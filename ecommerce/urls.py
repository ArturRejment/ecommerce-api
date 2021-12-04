from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from product.views import ProductViewSet

router = routers.SimpleRouter()
router.register(
    r'product',
    ProductViewSet,
    basename='product',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('cart/', include('cart.urls')),
    path('billing/', include('billing.urls')),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
