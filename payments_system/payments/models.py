from django.db import models


class Organization(models.Model):
    """
    Модель организаций.
    Поля:
    inn: ИНН,
    balance: Баланс.
    """
    inn = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)


class Payment(models.Model):
    """
    Модель платежей.
    Поля:
    operation_id: идентификатор операции
    amount: сумма, Руб.
    payer_inn: ИНН плательщика
    document_number: номер документа об оплате
    document_date: дата платежа
    created_at: дата создания объекта
    """
    operation_id = models.UUIDField(primary_key=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    payer_inn = models.CharField(max_length=12)
    document_number = models.CharField(max_length=64)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class BalanceLog(models.Model):
    """
    Модель для лога баланса.
    Поля:
    inn: ИНН
    old_balance: Старый баланс
    new_balance: Новый баланс
    changed_at: Дата изменения
    operation: ID операции (внешний ключ)
    """
    inn = models.CharField(max_length=12)
    old_balance = models.DecimalField(max_digits=14, decimal_places=2)
    new_balance = models.DecimalField(max_digits=14, decimal_places=2)
    changed_at = models.DateTimeField(auto_now_add=True)
    operation = models.ForeignKey(Payment, on_delete=models.CASCADE)
