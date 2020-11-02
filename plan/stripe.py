import logging
import stripe

from django.conf import settings


API_KEY = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)


class GoldMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_G_PLAN_MONTHLY_ID
        self.amount = 4000


class GoldQuaterPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_G_PLAN_QUATERLY_ID
        self.amount = 10000


class GoldAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_G_PLAN_ANNUAL_ID
        self.amount = 44000


class SilverMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_S_PLAN_MONTHLY_ID
        self.amount = 3000


class SilverQuaterPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_S_PLAN_QUATERLY_ID
        self.amount = 8000


class SilverAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_S_PLAN_ANNUAL_ID
        self.amount = 35000


class BronzeMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_B_PLAN_MONTHLY_ID
        self.amount = 1500


class BronzeQuaterPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_B_PLAN_QUATERLY_ID
        self.amount = 4000


class BronzeAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_B_PLAN_ANNUAL_ID
        self.amount = 17000


class GymPlan:
    def __init__(self, plan_id, plan_name):
        """
        """
        if plan_id == 'monthly':
            if plan_name == 'Gold':
                self.plan = GoldMonthPlan()
                self.id = 'monthly'
            elif plan_name == 'Silver':
                self.plan = SilverMonthPlan()
                self.id = 'monthly'
            else:
                self.plan = BronzeMonthPlan()
                self.id = 'monthly'
        elif plan_id == 'quaterly':
            if plan_name == 'Gold':
                self.plan = GoldQuaterPlan()
                self.id = 'quaterly'
            elif plan_name == 'Silver':
                self.plan = SilverQuaterPlan()
                self.id = 'quaterly'
            else:
                self.plan = BronzeQuaterPlan()
                self.id = 'quaterly'
        elif plan_id == 'annually':
            if plan_name == 'Gold':
                self.plan = GoldAnnualPlan()
                self.id = 'annually'
            elif plan_name == 'Silver':
                self.plan = SilverAnnualPlan()
                self.id = 'annually'
            else:
                self.plan = BronzeAnnualPlan()
                self.id = 'annually'
        else:
            raise ValueError('Invalid plan_id value')

        self.currency = 'gbp'

    @property
    def stripe_plan_id(self):
        return self.plan.stripe_plan_id

    @property
    def amount(self):
        return self.plan.amount


def set_paid_until(charge):
    logger.info(f"set_paid_until with {charge}")

    stripe.api_key = API_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email

        if customer:
            subscr = stripe.Subscription.retrieve(
                customer['subscriptions'].data[0].id
            )
            current_period_end = subscr['current_period_end']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.warning(
                f"User with email {email} not found"
            )
            return False

        user.set_paid_until(current_period_end)
        logger.info(
            f"Profile with {current_period_end} saved for user {email}"
        )
    else:
        pass
        # charge.amount  1990 | 19995
        # this was one time payment, update
        # paid_until (e.g. paid_until = current_date + 31 days) using
        # charge.paid + charge.amount attrs