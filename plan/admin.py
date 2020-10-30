from django.contrib import admin
from .models import Plan, UserMembership, Subscription


# Register your models here.
admin.site.register(Plan)
admin.site.register(UserMembership)
admin.site.register(Subscription)
