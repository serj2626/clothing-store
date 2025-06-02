from django.urls import path
from .views import ContactView, FeedbackView, FooterView

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("footer/", FooterView.as_view(), name="footer"),
]
