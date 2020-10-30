from django.contrib import admin

from .models import Individual_plan, Plan, Subscription

admin.site.register(Plan)
admin.site.register(Individual_plan)
admin.site.register(Subscription)

