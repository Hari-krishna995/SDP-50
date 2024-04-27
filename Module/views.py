
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Profile
from django.contrib.auth.models import User,auth
from django.shortcuts import  HttpResponse, redirect,render
from django.contrib import messages


def NewHomePage(request):
    return render(request, 'NewHomePage.html')

def home1(request):
    return render(request, 'starpage.html')


def Nutritiontip(request):
    return render(request, 'nutritiontips.html')

def pregnant(request):
    return render(request, 'pregnant.html')



def service(request):
    return render(request, 'service.html')


def articles(request):
    return render(request, 'articles.html')

def signup(request):
    return render(request, 'signup.html')



def login(request):
    return render(request, 'login.html')

def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, email=email, password=pass1)
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Account created successfully!!')
            return redirect('login')  # Redirect to login page after successful signup
    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('new_home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login1')
        else:
            messages.error(request, 'Please provide both username and password')
            return redirect('login1')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def About(request):
    return render(request, 'About us.html')


def recipe(request):
    return render(request, 'recipe.html')


def doctor_login(request):
    return HttpResponse("Doctor Login Page")


def admin_login(request):
    return HttpResponse("Admin Login Page")


def client_home(request):
    return render(request, 'client/home.html')


def doctor_home(request):
    return render(request, 'doctor/home.html')


def admin_home(request):
    return render(request, 'admins/home.html')


def home(request):
    return render(request, 'homepage.html')




def doclogin(request):
    return render(request, 'doctorlogin.html')
def doctorlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Doctor.objects.filter(name=username,password=password).exists():
            return render(request,'doctor/base_doctor.html')
        else:
            return HttpResponse("Wrong Password")
    return render(request,'doctorlogin.html')


from .form import AppointmentForm
from .models import Doctor

from django.contrib.auth.decorators import login_required

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.username = request.user.username
            appointment.save()
            return redirect('new_home')  # Redirect to NewHomePage after successful appointment booking
    else:
        form = AppointmentForm()
    doctors_with_specialization = Doctor.objects.all().values_list('id', 'name', 'specialization')
    return render(request, 'book_appointment.html', {'form': form, 'doctors': doctors_with_specialization})


# views.py


from .models import Appointment

def view_appointments(request):
    appointments = Appointment.objects.filter(username=request.user.username)
    return render(request, 'view_appointment.html', {'appointments': appointments})







