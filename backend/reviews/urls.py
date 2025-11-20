from .views import ReviewViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("reviews", ReviewViewSet, basename="reviews")

urlpatterns = router.urls