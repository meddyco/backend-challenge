from django.http import JsonResponse
from doctors.models import Doctor


def get_doctors(request):
	doctors = Doctor.objects.all()
	doctor_list = [doctor.serialize() for doctor in doctors]
	return JsonResponse({"data": doctor_list}, status=200)
