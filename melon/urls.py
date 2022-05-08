from django.urls import path
from . import views


app_name = 'melon'

urlpatterns = [
    path("chart/", views.chart, name="chart"),
]
