from rest_framework.viewsets import generics
from users.serializers import UserSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsOwnerForUser
from rest_framework.permissions import IsAdminUser


class UserCreateAPIView(generics.CreateAPIView):
    """View for creating user"""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        password = serializer.data['password']
        user = User.objects.get(email=serializer.data['email'])
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListAPIView(generics.ListAPIView):
    """View for displaying all users"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, ]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """View for displaying one chosen user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]


class UserUpdateAPIView(generics.UpdateAPIView):
    """View for user updating"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]


class UserDestroyAPIView(generics.DestroyAPIView):
    """View for deleting one chosen user"""
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]
