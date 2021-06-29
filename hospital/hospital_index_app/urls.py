from . import views
from django.urls import path


app_name = 'hospital_index_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('Doctors/<int:Doctors_id>/', views.details, name='details'),
    path('Blog/<int:Blog_id>/', views.blog_details,name='blog_details'),
    path('services/', views.services, name='services'),
    path('doctors_list/', views.doctors_list, name='doctors_list'),
    path('about/', views.about, name='about'),
    path('Register/', views.Register, name='Register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('confirm/', views.Confirm, name='confirm'),
    path('confirm_display/', views.confirm_display, name='confirm_display'),

]