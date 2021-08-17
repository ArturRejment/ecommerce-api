from django.urls import path
from .views import CartDetailView

urlpatterns = [
	path('<int:id>/', CartDetailView.as_view(), name='cart_detail')
]
