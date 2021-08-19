from django.urls import path
from .views import CartDetailView, ManageCartItems

urlpatterns = [
	path('', CartDetailView.as_view(), name='cart_detail'),
	path('cartitem/<int:id>/', ManageCartItems.as_view(), name='manage_cart_items')
]
