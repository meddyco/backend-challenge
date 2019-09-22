from django.urls import path
from doctors.views import get_doctors

urlpatterns = [
    path('doctors', get_doctors, name="doctor_list"),
]
