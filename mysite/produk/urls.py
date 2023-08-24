from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdukViewSet

router = DefaultRouter()
router.register(r'produk', ProdukViewSet)


app_name = "produk"
urlpatterns = [
    path('', include(router.urls)),
]
