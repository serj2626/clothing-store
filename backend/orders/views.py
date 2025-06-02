from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import stripe

from products.models import Cart

from .models import Order, OrderItem


# ===== STRIPE CHECKOUT =====
class StripeCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        order = Order.objects.create(user=request.user)

        line_items = []
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order, product=item.product, quantity=item.quantity
            )
            line_items.append(
                {
                    "price_data": {
                        "currency": "rub",
                        "product_data": {
                            "name": item.product.name,
                        },
                        "unit_amount": item.product.price * 100,
                    },
                    "quantity": item.quantity,
                }
            )

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=settings.DOMAIN + "/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=settings.DOMAIN + "/cancel",
        )

        order.stripe_checkout_id = session.id
        order.save()

        cart.items.all().delete()

        return Response({"checkout_url": session.url})
