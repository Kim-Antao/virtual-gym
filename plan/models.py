from django.db import models
from profiles.models import UserProfile

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
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username

