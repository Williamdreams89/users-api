from rest_framework import generics, permissions
from django.contrib.auth.models import User 
from main.api.serializers import UserSerializer

class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly
        permissions.AllowAny
    ]



