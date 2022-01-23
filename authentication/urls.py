from django.urls import path, include

from .views import ChangePasswordView

urlpatterns = [
	path('', include('djoser.urls')),
	path('', include('djoser.urls.authtoken')),
	path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
