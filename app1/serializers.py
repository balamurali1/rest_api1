from rest_framework.serializers import Serializer,CharField,DecimalField,\
	ValidationError,ModelSerializer 
from app1.models import Category,Product,SalesOrder
from rest_framework.response import Response	

#########Category Serializer ##########
class CategoryPostSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = ['name','id',]

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value

class CategoryPutSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = ['name','id',]

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value


##################Product serializer #########	
class ProductPostSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ['name','cost','category','id']

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value

class ProductPutSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ['name','cost','category','id']

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value
	
############ SalesOrder ##############	
class SalesOrderPostSerializer(ModelSerializer):
	class Meta:
		model = SalesOrder
		fields = ['description','products','id']

	def validate_description(self,value):
		if not value.isalnum():
			raise ValidationError("invalid description")
		return value	

class SalesOrderPutSerializer(ModelSerializer):
	class Meta:
		model = SalesOrder
		fields = ['description','products','id']

	def validate_description(self,value):
		if not value.isalnum():
			raise ValidationError("invalid description")
		return value

	


	

	


				



		


