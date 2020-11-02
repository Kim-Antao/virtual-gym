from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Plan, Service, SubscriberRegistration, PlanPricing
from .forms import SubsRegistrationForm
from .stripe import (GymPlan)


import stripe

API_KEY = settings.STRIPE_SECRET_KEY


def all_plan(request):
    plan = Plan.objects.all()
    service = Service.objects.all()
    context = {
        'plan': plan,
        'service': service,
    }
    return render(request, 'plan/plan.html', context)


def user_check(request, pid):
    if SubscriberRegistration.objects.filter(user=request.user):
        return render(request, 'plan/message.html')
    else:
        return redirect(subs_register, id=pid)


def subs_register(request, id):
    if request.method == 'POST':
        form = SubsRegistrationForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            goal = form.cleaned_data['goal']
            bmi = form.cleaned_data['bmi']
            pricing = Plan(id=id)
            current_plan = PlanPricing.objects.filter(planname=pricing)

            SubscriberRegistration.objects.create(user=request.user,
                                                  age=age,
                                                  height=height,
                                                  weight=weight,
                                                  gender=gender,
                                                  goal=goal,
                                                  bmi=bmi,
                                                  pricing=pricing,
                                                  )
            current_register = SubscriberRegistration.objects.get(user=request.user)
            context = {
                'current_register': current_register,
                'current_plan': current_plan,
            }
            return render(request, 'plan/plan_details.html', context)
    else:
        form = SubsRegistrationForm()
        template = 'plan/subs_registrations.html'
        context = {
            'form': form
        }
        return render(request, template, context)


@require_POST
@login_required
def payment_method(request):
    stripe.api_key = API_KEY
    planname = request.POST.get('payplanname')
    plan = request.POST.get('plan', 'monthly')
    automatic = request.POST.get('automatic', 'on')
    payment_method = 'card'

    planInst = GymPlan(plan_id=plan, plan_name=planname)
    print(planInst)
    context = {}
    payment_intent = stripe.PaymentIntent.create(
        amount=round(14.00*100),
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card']
    )
    if payment_method == "card":
        context['secret_key'] = payment_intent.client_secret
        context['customer_email'] = request.user.email
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        context['payment_intent_id'] = payment_intent.id
        context['automatic'] = automatic

        return render(request, 'plan/card.html', context)


@login_required
def card(request):
    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']

    stripe.api_key = API_KEY
    if automatic == 'on':
        # create subs
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id
        )
    return render(request, 'plan/thankyou.html')
