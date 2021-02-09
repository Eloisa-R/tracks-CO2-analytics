from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Shipments
from datetime import date, timedelta
from django.db.models import Avg, Sum

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")

def all(request):
    dt = date.today() - timedelta(70)
    output = []

    carrier_list = Shipments.objects.annotate(Avg('weight'), Sum('total_co2_emitted'), Sum('travelled_distance'))
    for data in carrier_list:
        output.append(
            {
            'carrier': data.carrier_company_id,
            'avg_weight':  data.weight__avg,
            'total_co2_emitted': data.total_co2_emitted__sum,
            'travelled_distance': data.travelled_distance__sum
            })
    return JsonResponse(output, safe=False)