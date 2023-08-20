from rest_framework.routers import DefaultRouter
from apps.watch.views import WatchViewSet, WatchCategoryViewSet, ReviewViewSet

router = DefaultRouter()

router.register('watches', WatchViewSet)
router.register('watch_category', WatchCategoryViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls