from django.urls import path
from .views import *
urlpatterns=[
    path('dashboard/',dashboard),
    path('orders/',order),
]