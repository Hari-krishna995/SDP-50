from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect




def home(request):
    return render(request, 'doctor/base_doctor.html')

def view_appointments(request):
    return render(request, 'doctor/view_appointments.html')



from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def doctor_dashboard(request):
    doctor = request.user.doctor
    appointment = Appointment.objects.filter(doctor=doctor).select_related('doctor')
    return render(request, 'doctor_dashboard.html', {'appointment': appointment})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def view_appointments(request):
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor/view_appointments.html', {'appointments': appointments})
