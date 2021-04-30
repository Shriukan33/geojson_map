from django.urls import path
from .views import MainMapView

app_name = 'carte'

urlpatterns = [
    path('', MainMapView.as_view(), name="main_map")
]