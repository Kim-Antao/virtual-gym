from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

import stripe

PLAN_CHOICES = (
    ('Bronze', 'br'),
    ('Silver', 'si'),
    ('Gold', 'go'),
)


class Plan(models.Model):
    plan_type = models.CharField(choices=PLAN_CHOICES, default='Bronze', max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.plan_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.object.get_or_create(user=instance)

    user_membership, created = UserMembership.objects.get_or_create(user=instance)

    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == "":
        new_customer_id = stripe.Customer.create(email=instance.email)
        bronze_plan = Plan.objects.get(plan_type='Free')
        user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.membership = free_membership
        user_membership.save()


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username

