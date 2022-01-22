from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ChangePasswordSerializer
from .models import User


class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={'password': ['Missing value for new_password or old_password']},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not self.object.check_password(serializer.data.get('old_password')):
            return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)

        self.object.set_password(serializer.data.get('new_password'))
        self.object.save()
        return Response({'new_password': ['New password created successfully.']})
