from django.http import JsonResponse
from doctors.models import Doctor
from django.db.models import Q

def get_listings(request):
	spec = request.GET.get('spec')
	lang = request.GET.get('lang')

	query = Q()

	if spec:
		query = Q(specialization__name__icontains=spec)
	if lang:
		query = Q(languages__name__icontains=lang)

	doctors = Doctor.objects.filter(query)

	doctor_list = [doctor.serialize() for doctor in doctors]
	return JsonResponse({"data": doctor_list}, status=200)
