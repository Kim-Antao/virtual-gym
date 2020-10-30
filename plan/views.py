from django.shortcuts import render
from .models import Plan


def all_plan(request):
    plan = Plan.objects.all()
    context = {
        'plan': plan,
    }
    return render(request, 'plan/plan.html', context)
