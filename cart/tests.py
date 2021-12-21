from decimal import Decimal

from rest_framework.test import APITestCase, APIClient

from cart.models import Cart, CartItem
from product.models import Product, Category, Season, Tag

CATEGORIES_NAMES = ['Mirror', 'Shoe', 'Table', 'Jacket', 'Pants']
SEASONS_NAMES = ['Zima', 'Lato']
TAGS_NAMES = ['tag1', 'tag2']

#
# class TestCartViews(APITestCase):
# 	""" Testing cart functionality """
#
# 	def setUp(self):
# 		categories = [Category.objects.create(category_name=category) for category in CATEGORIES_NAMES]
# 		seasons = [Season.objects.create(name=season) for season in SEASONS_NAMES]
# 		tags = [Tag.objects.create(name=tag) for tag in TAGS_NAMES]
# 		self.product_1 = Product.objects.create(
# 			product_name = 'Nike AirForce 1',
# 			retail_price_net=459.99,
# 			whole_price_net=409.99,
# 			detail_description='Best Nike model, soo comfy and good looking',
# 			availability=4,
# 			categories=categories[0],
# 			seasons=seasons[0],
# 			tags=tags[0],
# 			tax=23,
# 			stock_availability=10,
# 		)
# 		self.product_2 = Product.objects.create(
# 			product_name = 'Wrangler Stan Smith Collection',
# 			retail_price_net=250.99,
# 			whole_price_net=230,
# 			detail_description="Stunning jeans model from new Wrangler's cross collection.",
# 			availability=1,
# 			categories=categories[0],
# 			seasons=seasons[0],
# 			tags=tags[0],
# 			tax=23,
# 			stock_availability=10,
# 		)
# 		self.client.post(
# 			'/auth/users/',
# 			{
# 				'email': 'testuser@gmail.com',
# 				'password': 'StronGPassworD2115',
# 				're_password': 'StronGPassworD2115',
# 				'phone': '456153846',
# 				'first_name': 'Test',
# 				'last_name': 'Tester'
# 			},
# 			headers={
# 				'Content-Type': 'application/x-www-form-urlencoded'
# 			}
# 		)
# 		token_response = self.client.post(
# 			'/auth/token/login/',
# 			{
# 				'email': 'testuser@gmail.com',
# 				'password': 'StronGPassworD2115'
# 			},
# 			headers={
# 				'Content-Type': 'application/x-www-form-urlencoded'
# 			}
# 		)
# 		# Save auth token
# 		token = token_response.data.get('auth_token')
# 		# Set generated token as default authentication
# 		self.requestClient = APIClient()
# 		self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + token
#
# 	def testAddingProductToCart(self):
# 		response = self.client.post(
# 			f'/cart/{self.product_1.id}/add/'
# 		)
# 		self.assertEquals(response.status_code, 200)
# 		response_data = response.data
# 		self.assertEquals(response_data.get('get_products_quantity'), 1)
#
# 	def testRemovingProductFromCart(self):
# 		response = self.client.post(
# 			f'/cart/{self.product_1.id}/remove/'
# 		)
# 		self.assertEquals(response.status_code, 200)
# 		response_data = response.data
# 		self.assertEquals(response_data.get('get_products_quantity'), 0)
#
# 	def testCartFunctionality(self):
# 		# Add product two times
# 		self.client.post(
# 			f'/cart/{self.product_1.id}/add/'
# 		)
# 		response = self.client.post(
# 			f'/cart/{self.product_1.id}/add/'
# 		)
# 		# Check cart info
# 		self.assertEquals(response.status_code, 200)
# 		self.assertEquals(response.data.get('get_products_quantity'), 2)
# 		self.assertEquals(
# 			response.data.get('get_cart_total'),
# 			Decimal(str(self.product_1.product_price + self.product_1.product_price))
# 		)
# 		response = self.client.post(
# 			f'/cart/{self.product_2.id}/add/'
# 		)
# 		self.assertEquals(response.status_code, 200)
# 		self.assertEquals(response.data.get('get_products_quantity'), 3)
# 		self.assertEquals(
# 			response.data.get('get_cart_total'),
# 			Decimal(str(self.product_1.product_price + self.product_1.product_price + self.product_2.product_price))
# 		)
# 		response = self.client.post(
# 			f'/cart/{self.product_1.id}/remove/'
# 		)
# 		self.assertEquals(response.status_code, 200)
# 		self.assertEquals(response.data.get('get_products_quantity'), 2)
# 		self.assertEquals(
# 			response.data.get('get_cart_total'),
# 			Decimal(str(self.product_1.product_price + self.product_2.product_price))
# 		)
