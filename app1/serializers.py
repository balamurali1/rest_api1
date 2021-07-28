from rest_framework.serializers import Serializer,CharField,DecimalField,\
	ValidationError 
from app1.models import Category,Product,SalesOrder
from rest_framework.response import Response	

#########Category Serializer ##########
class CategoryGetSerializer(Serializer):
	name = CharField(max_length=250)

class CategoryPostSerializer(Serializer):
	name = CharField(max_length=250)

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value
	
	def save(self):
		cat = Category(name=self.data.get('name'))
		try:
			cat.save()
			message="Category %s inserted successfully" % cat.name
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)

class CategoryPutSerializer(Serializer):
	name = CharField(max_length=250)

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value

	def save(self):
		cat1 = Category(name=self.data.get(id=cat_id))
		try:
			cat1.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

class CategoryDeleteSerializer(Serializer):
	pass

##################Product serializer #########	
class ProductGetSerializer(Serializer):
	name = CharField(max_length=250)
	cost = DecimalField(max_digits=8,decimal_places=2)

class ProductPostSerializer(Serializer):
	name = CharField(max_length=250)
	cost = DecimalField(max_digits=8,decimal_places=2)

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("invalid name")
		return value

	def validate_cost(self,value):
		if not value.isdigit():
			raise ValidationError("invalid cost")
		return value	

	def save(self):

		try:
			cat = Category.objects.get(id=2)
			pro = Product(name=self.data.get('name'),cost=self.data.get('cost'),category=cat)
			pro.save()
			message="Product %s%s inserted successfully" % pro.name,pro.cost,pro.category
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)

class ProductPutSerializer(Serializer):
	pass


class ProductDeleteSerializer(Serializer):
	pass


############ SalesOrder ##############	
class SalesOrderGetSerializer(Serializer):
	description = CharField(max_length=600)

class SalesOrderPostSerializer(Serializer):
	description = CharField(max_length=600)

	def validate_description(self,value):
		if not value.isalnum():
			raise ValidationError("invalid description")
		return value

	def save(self):
		try:
			sale = SalesOrder(description=self.data.get('description'))
			sale.save()

			for prod_id in data.get("products"):	
				prod = Product.objects.get(id=prod_id)
				sale.products.add(prod)
				
			message="SalesOrder %s inserted successfully" % sale.description
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)


class SalesOrderPutSerializer(Serializer):
	pass


class SalesOrderDeleteSerializer(Serializer):
	pass 				




	

	


				



		


