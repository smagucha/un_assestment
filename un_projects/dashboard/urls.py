from django.urls import path, include
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('addemployee/', views.create_staff_member, name='addemployee')
]