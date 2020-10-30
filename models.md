Model Architecture planning

plan
    -plan_type  (bronze, silver, gold)
    -price
    -stripe plan id


services:
    - service-type (excercise plan, nutrution plan)

Subscription via Stripe
    - Pricing - (price per month) 
    - currency 
    - id 
    - name (bronze, silver, gold)   (FK)

Subscription 
    - User (FK) 
    - stripe_subscription_id 
    - status (active / canceled / past_due / trialing) 
    - Pricing (FK)