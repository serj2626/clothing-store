from django.urls import path

from .views import ContactView, FAQListView, FeedbackView, FooterView, SubscriptionView

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("subscription/", SubscriptionView.as_view(), name="feedback"),
    path("footer/", FooterView.as_view(), name="footer"),
    path("faq/", FAQListView.as_view(), name="faq-list"),
]
