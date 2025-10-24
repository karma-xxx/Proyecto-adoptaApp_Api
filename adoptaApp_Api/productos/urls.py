from rest_framework.routers import DefaultRouter
from .views import ProductosViewSet

router = DefaultRouter()
router.register(r'productos', ProductosViewSet, basename='productos')

urlpatterns = router.urls
