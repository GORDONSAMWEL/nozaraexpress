from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can manage users



from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

