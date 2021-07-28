from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Category
from app1.models import Product
from app1.models import SalesOrder
from app1.serializers import CategoryGetSerializer,CategoryPostSerializer,\
	CategoryPutSerializer,CategoryDeleteSerializer,ProductGetSerializer,\
	ProductPostSerializer,ProductPutSerializer,ProductDeleteSerializer,\
	SalesOrderGetSerializer,SalesOrderPostSerializer,SalesOrderPutSerializer,\
	SalesOrderDeleteSerializer
import json

# Create your views here.

############ Category #############
class CategoryAPIView(APIView):

    ##########get method########
	def get(self,request,cat_id=None):
		items = []
		cats = []
		status_code=200
		data = {"message":"Success","items":items}
		if cat_id:
			try:
				cats = Category.objects.get(id=cat_id)
				if cats:
					cats = [cats]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			cats = Category.objects.all()
			cat_ser = CategoryGetSerializer(cats,many=True)	
		return Response(cat_ser.data,status=status_code)

	#########Post(insert)###########
	def post(self,request):
		ser = CategoryPostSerializer(data = request.data)
		if ser.is_valid():
			resp = ser.save()
			return resp
		else:	
			return Response({"message":ser.errors},status=400)		

    ###########PUT (update)###########
	def put(self,request,cat_id):

		data = {"message":"Success"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			ser1 = CategoryPutSerializer(cat,data = request.data)
			data = {}
			if ser1.is_valid():
				ser1.save()
				return Response(data=data)

			#cat = Category.objects.get(id=cat_id)
			#request_data = request.data
			# cat.name = request_data.get("name")
			# cat.save()

		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

    ############Delete##########
	def delete(self,request,cat_id):
		data = {"message":"Delete successfully"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			cat.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

################### PRODUCT ###################
class ProductAPIView(APIView):

	########## Post method (Insert) ########
	def post(self,request):
		ser = ProductPostSerializer(data=request.data)
		if ser.is_valid():
			resp = ser.save()
			return resp
		else:	
			return Response({"message":ser.errors},status=400)

		# data = request.data

		# try:
		# 	cat = Category.objects.get(id=2)
		# 	pro = Product(name=data.get('name'),cost=data.get('cost'),category=cat)
		# 	pro.save()
		# 	message="Product %s%s inserted successfully" % pro.name,pro.cost,pro.category
		# 	#raise Exception('Category not Created.')
		# 	status_code = 200
		# except Exception as err:
		# 	message = str(err)
		# 	status_code=400	
		# return Response({"message":message},status= status_code)

    ##########get method########
	def get(self,request,pro_id=None):
		items = []
		pros = []
		status_code=200
		data = {"message":"Success","items":items}
		if pro_id:
			try:
				pros = Product.objects.get(id=pro_id)
				if pros:
					pros = [pros]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			pros = Product.objects.all()
			pro_ser = ProductGetSerializer(pros,many=True)
		return Response(pro_ser.data,status=status_code)		

     #################PUT (update)###############
	def put(self,request,pro_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			pro = Product.objects.get(id=pro_id)
			request_data = request.data
			pro.name = request_data.get("name")
			pro.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

     ############Delete##########
	def delete(self,request,pro_id):
		data = {"message":"Delete successfully!!!!"}
		status_code = 200
		try:
			pro = Product.objects.get(id=pro_id)
			pro.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)



############## SalesOrder #############

class SalesAPIView(APIView):
	##########Post method########
	def post(self,request):
		ser = SalesOrderPostSerializer(data = request.data)
		if ser.is_valid():
			resp = ser.save()
			return resp
		else:	
			return Response({"message":ser.errors},status=400)
		
	 ##########get method########
	def get(self,request,sal_id=None):
		items = []
		sales = []
		status_code=200
		data = {"message":"Success","items":items}
		if sal_id:
			try:
				sales = SalesOrder.objects.get(id=sal_id)
				if sales:
					sales = [sales]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			sales = SalesOrder.objects.all()
			sales_ser = SalesOrderGetSerializer(sales,many=True)

		return Response(sales_ser.data,status=status_code)	

	 #################PUT (update)###############
	def put(self,request,sal_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			sale = SalesOrder.objects.get(id=sal_id)
			request_data = request.data
			sale.description = request_data.get("description")
			sale.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)
	

	 ############Delete##########
	def delete(self,request,sal_id):
		data = {"message":"Delete successfully!!!!"}
		status_code = 200
		try:
			sale = SalesOrder.objects.get(id=sal_id)
			sale.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)	






