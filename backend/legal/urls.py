from django.urls import path

from .views import (
    AboutView,
    CookiePolicyView,
    ExchangeAndReturnPageView,
    OffertaView,
    PolicyView,
)

urlpatterns = [
    path("cookie-policy/", CookiePolicyView.as_view(), name="cookie-policy"),
    path("about-company/", AboutView.as_view(), name="about-company"),
    path("offerta/", OffertaView.as_view(), name="offerta"),
    path("policy/", PolicyView.as_view(), name="policy"),
    path(
        "exchange-and-return/",
        ExchangeAndReturnPageView.as_view(),
        name="exchange-and-return",
    ),
]
