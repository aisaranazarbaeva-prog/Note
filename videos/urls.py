from .views import NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'videos', NewsViewSet)
urlpatterns = router.urls