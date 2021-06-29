# from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
# from django.urls import reverse

from .models import Doctors, Blog, Booking
from django.contrib import messages, auth
from django.contrib.auth.models import User


# from . models import Blog


# Create your views here.
def index(request):
    doctors_list = Doctors.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'doctors_list': doctors_list, 'blogs': blogs})


def details(request, Doctors_id):
    Doctor = Doctors.objects.get(id=Doctors_id)
    return render(request, 'doctor_details.html', {'Doctor': Doctor})


def blog_details(request, Blog_id):
    Blogs = Blog.objects.get(id=Blog_id)
    return render(request, 'blog_details.html', {'Blogs': Blogs})


def doctors_list(request):
    doctor_list = Doctors.objects.all()
    return render(request, 'doctors_list.html', {'doctor_list': doctor_list})


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('hospital_index_app:Register')
            elif User.objects.filter(username=email).exists():
                messages.info(request, "Username already exist")
                return redirect('hospital_index_app:Register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print("Your registration finished")
                messages.info(request, "user created successfully ")
                return redirect('hospital_index_app:login')
        else:
            messages.warning(request, "password is not matching!")

    else:

        return render(request, 'registration.html', )


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "lodged in Successfully ")
            print('lodged in')
            return redirect('/')
        else:
            messages.info(request, "user invalid")
            return redirect('login')
    else:
        return render(request, "login.html")


def log_out(request):
    auth.logout(request)
    return redirect('/')


def Confirm(request):
    doctors_list_new = Doctors.objects.all()
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        time_slot = request.POST.get('time_slot')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')

        booking = Booking(patient_name=patient_name, age=age, phone=phone, time_slot=time_slot, department=department,
                          doctor=doctor)
        booking.save()
        print('booking done')
        return redirect('hospital_index_app:confirm_display')
    else:
        return render(request, "booking.html", {'doctors_list_new': doctors_list_new})


def confirm_display(request, id=id):
    Booking_view = Booking.objects.all()
    return render(request, "booking_details.html", {'Booking_view': Booking_view})
