from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs de la app
    path('', views.home, name='home'),
    path('info/', views.ver_info_bike_santiago, name='info'),
]
