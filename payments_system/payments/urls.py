from django.urls import path
from .views import bank_webhook, get_balance

urlpatterns = [
    path('webhook/bank/', bank_webhook),
    path('organizations/<str:inn>/balance/', get_balance),
]
