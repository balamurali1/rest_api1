from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from app1.models import Category
from app1.models import Product
from app1.models import SalesOrder
from app1.serializers import CategoryPostSerializer,CategoryPutSerializer,\
	ProductPostSerializer,ProductPutSerializer,SalesOrderPostSerializer,SalesOrderPutSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView	
import json

# Create your views here.

############ Category #############
class CategoryListCreateAPIView(ListCreateAPIView):
	serializer_class = CategoryPostSerializer
	queryset = Category.objects.all()

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = CategoryPutSerializer
	queryset = Category.objects.all()	


################### PRODUCT ###################
class ProductListCreateAPIView(ListCreateAPIView):
	serializer_class = ProductPostSerializer
	queryset = Product.objects.all()

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = ProductPutSerializer
	queryset = Product.objects.all()	

	

############## SalesOrder #############
class SalesOrderListCreateAPIView(ListCreateAPIView):
	serializer_class = SalesOrderPostSerializer
	queryset = SalesOrder.objects.all()

class SalesOrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = SalesOrderPutSerializer
	queryset = SalesOrder.objects.all()	




