from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

user = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name


class SubscriberRegistration(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    gender = models.CharField(max_length=10)
    goal = models.CharField(max_length=20)
    bmi = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    customer_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


class Service(models.Model):
    pricing_tiers = models.ForeignKey(Plan, blank=True,
                                      on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    pricing = models.ForeignKey(Plan, on_delete=models.CASCADE,
                                related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
