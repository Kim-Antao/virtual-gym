from django.contrib import admin

from .models import Course, Video, Plan

admin.site.register(Plan)
admin.site.register(Course)
admin.site.register(Video)

