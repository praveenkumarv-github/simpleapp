from django.urls import path
from .views import generate_password, index, health_check

urlpatterns = [
    path('', index, name='index'),
    path('generate-password/', generate_password, name='generate_password'),
    path('healthz/', health_check, name='health_check'),
]