from django.urls import path
from src.views import slider_view

urlpatterns = [
    path('', slider_view, name='slider'),
]