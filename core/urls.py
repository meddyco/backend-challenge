"""
Core URL Configurations
"""
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include(('doctors.urls', 'doctors'), namespace='doctors')),
]
