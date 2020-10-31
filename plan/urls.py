from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plan, name='plan'),
    path('register/', views.subs_register, name='subs_register'),
]
