import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .serializers import CartSerializer, WishlistSerializer, ProductSerializer
from .models import Cart, Wishlist, CartItem, Product

stripe.api_key = settings.STRIPE_SECRET_KEY


TAG = "Товары и Корзина"


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(tags=[TAG], summary="Список товаров")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(tags=[TAG], summary="Детали товара")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# ===== ИЗБРАННОЕ =====
class WishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Wishlist.objects.filter(user=request.user)
        data = WishlistSerializer(items, many=True).data
        return Response(data)

    def post(self, request):
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        Wishlist.objects.get_or_create(user=request.user, product=product)
        return Response({"status": "added"})


# ===== КОРЗИНА =====
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        data = CartSerializer(cart).data
        return Response(data)

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity = quantity
        item.save()
        return Response({"status": "updated"})



# import stripe
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.views import View

# stripe.api_key = settings.STRIPE_SECRET_KEY

# @csrf_exempt
# def create_checkout_session(request):
#     import json
#     data = json.loads(request.body)

#     try:
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=data['items'],
#             mode='payment',
#             success_url=data['success_url'],
#             cancel_url=data['cancel_url'],
#         )
#         return JsonResponse({'id': session.id})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)



# 🖼 ЧАСТЬ 2: Nuxt 3 (frontend)
# 1. Установка Stripe JS SDK:

# npm install @stripe/stripe-js



# 2. Настрой .env и nuxt.config.ts
# .env:


# STRIPE_PK=pk_test_...
# API_BASE_URL=http://localhost:8000

# export default defineNuxtConfig({
#   runtimeConfig: {
#     public: {
#       stripePk: process.env.STRIPE_PK,
#       apiBase: process.env.API_BASE_URL
#     }
#   }
# })


#  Код для оплаты
# pages/checkout.vue (пример):


# <template>
#   <button @click="checkout">Оплатить</button>
# </template>

# <script setup>
# import { loadStripe } from '@stripe/stripe-js'

# const config = useRuntimeConfig()

# const checkout = async () => {
#   const stripe = await loadStripe(config.public.stripePk)

#   const { data } = await useFetch('/api/checkout/', {
#     baseURL: config.public.apiBase,
#     method: 'POST',
#     body: {
#       items: [
#         {
#           price_data: {
#             currency: 'usd',
#             product_data: {
#               name: 'Футболка',
#             },
#             unit_amount: 2500,
#           },
#           quantity: 1,
#         }
#       ],
#       success_url: window.location.origin + '/success',
#       cancel_url: window.location.origin + '/cancel'
#     }
#   })

#   await stripe.redirectToCheckout({ sessionId: data.value.id })
# }
# </script>