from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

import datetime
from datetime import date

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

user = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class PlanPricing(models.Model):
    planname = models.ForeignKey(Plan, on_delete=models.CASCADE)
    period = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=False)

    def __str__(self):
        return self.period


class SubscriberRegistration(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    gender = models.CharField(max_length=10)
    goal = models.CharField(max_length=20)
    bmi = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    pricing = models.ForeignKey(Plan, on_delete=models.CASCADE,
                                related_name='subscriptions')
    paid_until = models.DateField(null=True, blank=True)

    def set_paid_until(self, date_or_timestamp):
        if isinstance(date_or_timestamp, int):
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        self.save()

    def has_paid(self, current_date=datetime.date.today()):
        if self.paid_until is None:
            return False
        return current_date < self.paid_until

    def __str__(self):
        return self.user.email


class Service(models.Model):
    pricing_tiers = models.ForeignKey(Plan, blank=True,
                                      on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

