function card(STRIPE_PUBLIC_KEY,customer_email){
    document.addEventListener("DOMContentLoaded", function(event){
        var stripe = Stripe(STRIPE_PUBLIC_KEY);
        var elements = stripe.elements();

        var style = {
            base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
                }
            },
            invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
            }
        };
        var card = elements.create('card', {style: style});
        card.mount('#card-element1');

        card.addEventListener('change',function(event){
            var displayError = document.getElementById('card-errors1');
            if(event.error){
                displayError.textContent = event.error.message;
            }else{
                displayError.textContent = '';
            }
        });

        var form = document.getElementById('payment-form');
        form.addEventListener('submit',function(event){
            event.preventDefault();
            stripe.createToken(card).then(function(result){
                if(result.error){
                    var errorElement = document.getElementById('card-errors1');
                    errorElement.textContent = result.error.message;
                }else{
                    stripe.createPaymentMethod({
                        type:'card',
                        card: card,
                        billing_details:{
                            email: customer_email,
                        },
                    }).then(function(payment_method_result){
                        if(payment_method_result.error){
                            var errorElement = document.getElementById('card-errors1');
                            errorElement.textContent = payment_method_result.error.message;
                        }else{
                            var form = document.getElementById('payment-form');
                            var hiddenInput = document.createElement('input');

                            hiddenInput.setAttribute('type', 'hidden');
                            hiddenInput.setAttribute('name', 'payment_method_id');
                            hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

                            form.appendChild(hiddenInput);
                            form.submit();
                        }
                    });
                }
            });
        });

    });
}