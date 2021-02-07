from django.conf.urls import url
from catalog import views


urlpatterns = [
    url(r'^api/public/', views.public)
]