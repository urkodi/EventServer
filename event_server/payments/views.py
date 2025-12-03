import stripe
import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import traceback 

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
@require_http_methods(["POST"])
def create_checkout_session(request):
    try:
        
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
            # payment completion page
            return_url=f"{settings.FRONTEND_URL}/booking-confirmation?session_id={{CHECKOUT_SESSION_ID}}",
        )
        
        return JsonResponse({
            'checkoutSessionClientSecret': session['client_secret']
        })
        
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=400)
