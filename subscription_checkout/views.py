from django.shortcuts import render


# Create your views here.
def subscription_checkout(request):
    template = 'subscription_checkout/subscription_checkout.html'
    context = {

    }
    return render(request, template, context)
