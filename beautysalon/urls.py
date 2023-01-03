from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email_save_contact_form/', views.email_save_contact_form, name='email_save_contact_form'),
]
