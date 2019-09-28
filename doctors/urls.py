from django.urls import path
from doctors.views import get_listings

urlpatterns = [
    path('doctors', get_listings, name="doctor_list"),
    path('clinics', get_listings, name="clinic_list"),
]
