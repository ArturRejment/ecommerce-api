import datetime

import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class LoginView(APIView):

	def post(self, request):
		username = request.data.get('email', None)
		password = request.data.get('password', None)
		user = User.objects.get(username=username)

		if user is None:
			raise AuthenticationFailed('Incorrect username or password')

		if not user.check_password(password):
			raise AuthenticationFailed('Incorrect username or password')

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
			'iat': datetime.datetime.utcnow()
		}

		token = token.encode(password, 'secret', algorithm='HS256').decode('utf-8')

		return Response({
			'jwt': token
		})
