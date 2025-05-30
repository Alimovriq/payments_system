from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED,)
from .models import Organization, Payment, BalanceLog
from .serializers import WebhookSerializer


@api_view(["POST"])
def bank_webhook(request):
    """
    Представление для вебхуков от банка.
    """
    data = request.data
    operation_id = data.get("operation_id")
    serilizator = WebhookSerializer(data=data)

    if operation_id is None:
        return Response(
            {"status": "Отсутствует id операции"}, status=HTTP_400_BAD_REQUEST)

    if Payment.objects.filter(operation_id=operation_id).exists():
        return Response({"status": "Успешно"}, status=HTTP_200_OK)

    if not serilizator.is_valid():
        return Response(serilizator.errors, status=HTTP_400_BAD_REQUEST)

    payment = serilizator.save()

    org, _ = Organization.objects.get_or_create(inn=payment.payer_inn)
    old_balance = org.balance
    org.balance += payment.amount
    org.save()

    # Лог в отдельную таблицу
    BalanceLog.objects.create(
        inn=org.inn,
        old_balance=old_balance,
        new_balance=org.balance,
        operation=payment
    )

    return Response({"status": "Успешно"}, status=HTTP_201_CREATED)


@api_view(["GET"])
def get_balance(request, inn):
    """
    Представление для запросов баланса организации по ИНН.
    """
    try:
        org_obj = Organization.objects.get(inn=inn)
    except Organization.DoesNotExist:
        return Response({"error": "Организация не найдена"}, status=HTTP_404_NOT_FOUND)

    org_inn = org_obj.inn
    org_balance = org_obj.balance

    return Response(data={"inn": org_inn, "balance": org_balance})
