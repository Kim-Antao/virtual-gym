from django.shortcuts import render
from .models import Plan, Service


def all_plan(request):
    plan = Plan.objects.all()
    service = Service.objects.all()
    context = {
        'plan': plan,
        'service': service,
    }
    return render(request, 'plan/plan.html', context)
