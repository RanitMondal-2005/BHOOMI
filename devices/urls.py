# devices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Devices Home page
    path('devices/', views.device_list, name='device_list'),
    # Add a Device
    path('devices/add/', views.add_device, name='add_device'),
    # Remove that Specific Device
    path('devices/<int:device_id>/delete/', views.delete_device, name='delete_device'),
]
