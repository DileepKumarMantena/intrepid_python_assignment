from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers


urlpatterns = [



    path('dashboard-items-html/', dashboard_items, name='dashboard_items'),
    path('bookings-html/', bookings, name='bookings'),
    path('', packages, name='packages'),
    path('packages/<int:package_id>/edit/', edit_package, name='edit_package'),
    
    path('delete/<int:package_id>/', delete_package, name='delete_package'),

    path('packages/add/', add_package, name='add_package'),

]