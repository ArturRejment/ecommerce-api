from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
	path('list/', ProductListView.as_view(), name='product_list_view'),
	path('<int:id>/', ProductDetailView.as_view({'get': 'retrieve'}), name='product_detail_view')
]
