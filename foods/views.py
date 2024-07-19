from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
from .serializers import FoodSerializers, CategorySerializers
from .models import Food, Category

class Createfood(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class listfood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]

class Updatefood(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class deletefood(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

class createcategory(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

class listcategory(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers


class Updatecategory(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class deletecategory(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]