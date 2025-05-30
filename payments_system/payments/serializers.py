from rest_framework import serializers
from .models import Payment


class WebhookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вебхука.
    """
    class Meta:
        model = Payment
        fields = [
            'operation_id',
            'amount',
            'payer_inn',
            'document_number',
            'document_date',
        ]
