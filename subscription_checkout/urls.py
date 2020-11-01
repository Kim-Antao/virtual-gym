from django.urls import path
from . import views


urlpatterns =[    
    path('', views.subscription_checkout, name='subscription_checkout'),
]