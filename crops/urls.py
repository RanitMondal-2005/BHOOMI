# crops/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Crop List of all 20 crops
    path('crops/', views.crop_list, name='crop_list'),
    # Individual Crop Details
    path('crops/<str:crop_name>/', views.crop_detail, name='crop_detail'), # That <str:crop_name> is a URL converter — it tells Django “whatever text appears in this position of the URL, capture it as a string and pass it into the view as a parameter named 'crop_name'
]
