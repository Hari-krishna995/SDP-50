from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),

    # Add more URLs as needed
]

