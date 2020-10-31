from django.shortcuts import render
from django.conf import settings
from .models import Plan, Service, SubscriberRegistration
from .forms import SubsRegistrationForm
import stripe

stripe.api_key = settings.STRIPE_PUBLIC_KEY


def all_plan(request):
    plan = Plan.objects.all()
    service = Service.objects.all()
    context = {
        'plan': plan,
        'service': service,
    }
    return render(request, 'plan/plan.html', context)


def subs_register(request):
    if request.method == 'POST':
        form = SubsRegistrationForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            goal = form.cleaned_data['goal']
            bmi = form.cleaned_data['bmi']

            SubscriberRegistration.objects.create(user=request.user,
                                                  age=age,
                                                  height=height,
                                                  weight=weight,
                                                  gender=gender,
                                                  goal=goal,
                                                  bmi=bmi,
                                                  )
    form = SubsRegistrationForm()
    template = 'plan/subs_registrations.html'
    context = {
        'form': form
    }
    return render(request, template, context)
