from django.contrib import admin

from .models import Plan, Service, SubscriberRegistration, PlanPricing

admin.site.register(Plan)
admin.site.register(Service)
admin.site.register(SubscriberRegistration)
admin.site.register(PlanPricing)
