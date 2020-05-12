from decimal import Decimal
from django.conf import settings
from orders.models import Product

class Cart(object):
	def __init__(self, request):
	#Initialize the cart.
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, topping, quantity=1, override_quantity=False):
		topping_list = []
		topping_price = Decimal(0)
		if topping != None:
			if topping.count() != 0:
				print(topping)
				for value in topping:
					topping_list.append(value.name)
					topping_price += value.price
		if len(topping_list) >=5:
			topping_list.append("(Special Pizza!)")
		#Add a product to the cart or update its quantity.
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0,'topping_list': topping_list,'topping_price':str(topping_price), 'price': str(product.price)}
		if override_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
			self.cart[product_id]['topping_list'] = topping_list
			self.cart[product_id]['topping_price'] = str(topping_price)
		self.save()

	def save(self):
		# mark the session as "modified" to make sure it gets saved
		self.session.modified = True

	def remove(self, product):
		#Remove a product from the cart.
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		#Iterate over the items in the cart and get the products from the database.
		product_ids = self.cart.keys()
		# get the product objects and add them to the cart
		products = Product.objects.filter(id__in=product_ids)
		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)]['product'] = product
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			if len(item['topping_list']) >=6:
				item['total_price'] = round((((item['price'] + Decimal(item['topping_price'])) * item['quantity'])* Decimal(0.95)),2)
			else:
				item['total_price'] = ((item['price'] + Decimal(item['topping_price'])) * item['quantity'])
			yield item

	def __len__(self):
		#Count all items in the cart.
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		total=[]
		for item in self.cart.values():
			if len(item['topping_list']) >=6:
				total.append(round((((Decimal(item['price']) + Decimal(item['topping_price'])) * item['quantity'])* Decimal(0.95)),2))
			else:
				total.append(((Decimal(item['price']) + Decimal(item['topping_price'])) * item['quantity']))
		return sum(total)

	def clear(self):
		# remove cart from session
		del self.session[settings.CART_SESSION_ID]
		self.save()
