from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from product.views import ProductViewSet, ProductCrudViewSet
from cart.views import CartView
from order.views import OrderViewSet

router = routers.SimpleRouter()

router.register(
    r'product',
    ProductViewSet,
    basename='product',
)

router.register(
    r'cart',
    CartView,
    basename='cart',
)

router.register(
    r'product-management',
    ProductCrudViewSet,
    basename='product-management',
)

router.register(
    r'order',
    OrderViewSet,
    basename='order',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('billing/', include('billing.urls')),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
