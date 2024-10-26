"""
URL configuration for RestaurantApp app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('testpage/', views.testpage, name='TestPage'),
    # here for testing PLEASE dont touch
]
