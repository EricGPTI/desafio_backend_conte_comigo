from api.views import CalculationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('calculations', CalculationViewSet)
urlpatterns = router.urls