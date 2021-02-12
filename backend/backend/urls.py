from django.conf.urls import url
from shipments import views


urlpatterns = [url(r"^api/carriers/all", views.all)]
