import stripe
import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
@require_http_methods(["POST"])
def create_checkout_session(request):
    try:
        # Parse request body
        data = json.loads(request.body)
        
        # Create Checkout Session 
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": "T-shirt"},
                        "unit_amount": 2000,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            ui_mode="custom",
            # The URL of payment completion page
            return_url="https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
        )
        
        return JsonResponse({
            'checkoutSessionClientSecret': session['client_secret']
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)
