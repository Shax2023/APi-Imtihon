from .serializers import ProductSerializer, Order_itemSerializer, OrderSerializer, UserSerializer
from rest_framework.views import APIView
from .models import  Product, User, Order, Order_item
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.permissions import IsAdminUser,AllowAny
from django.shortcuts import get_object_or_404



class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class UserList(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrdeList(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemList(ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer
