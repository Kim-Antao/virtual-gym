from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plan, name='plan'),
    path('register/<id>', views.subs_register, name='subs_register'),
    path('checks/<pid>', views.user_check, name='user_check'),
    path('paymentMethod/', views.payment_method, name='payment_method'),
    path('successMessage/', views.card, name='card'),
]
