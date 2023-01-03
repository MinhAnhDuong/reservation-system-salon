from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_information, name='basicinfo'),
    path('selectdate/', views.select_date, name='selectdate'),
    path('selecttime/', views.select_time, name='selecttime'),
    path('save/', views.save, name='save'),
    path('reservationslist/', views.all_reservations, name='reservationslist'),
    path('reservationslist/delete/<int:id>/', views.delete_reservation, name='deletereservation')
]
