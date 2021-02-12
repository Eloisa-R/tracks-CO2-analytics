from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Shipments
from datetime import date, timedelta
from django.db.models import Avg, Sum


def all(request):
    last_10_weeks = date.today() - timedelta(70)

    output = []

    carrier_list = Shipments.objects.values("carrier_company_id").annotate(
        Avg("weight"), Sum("total_co2_emitted"), Sum("travelled_distance")
    )
    for data in carrier_list:
         output.append(data)
    return JsonResponse(output, safe=False)
