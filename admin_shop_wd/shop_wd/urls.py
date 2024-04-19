# myapp/urls.py

from django.urls import path
from .views import send_message_view

urlpatterns = [
    path('send_message/', send_message_view, name='send_message'),
]
