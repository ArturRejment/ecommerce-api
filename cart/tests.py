from rest_framework.test import APITestCase, APIClient

from cart.models import Cart, CartItem
from product.models import Product, Category

CATEGORIES_NAMES = ['Mirror', 'Shoe', 'Table', 'Jacket', 'Pants']

class TestCartViews(APITestCase):
	""" Testing cart funcionality """

	def setUp(self):
		categories = [Category.objects.create(category_name=category) for category in CATEGORIES_NAMES]
		product_1 = Product.objects.create(
			product_name = 'Nike AirForce 1',
			product_price=459.99,
			detail_description='Best Nike model, soo comfy and good looking',
			availability=4,
		)
		product_2 = Product.objects.create(
			product_name = 'Wrangler Stan Smith Collection',
			product_price=250.99,
			detail_description="Stunning jeans model from new Wrangler's cross collection.",
			availability=1,
		)
		self.client.post(
			'/auth/users/',
			{
				'email': 'testuser@gmail.com',
				'password': 'StronGPassworD2115',
				're_password': 'StronGPassworD2115',
				'phone': '456153846',
				'first_name': 'Test',
				'last_name': 'Tester'
			},
			headers={
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		)
		token_response = self.client.post(
			'/auth/token/login/',
			{
				'email': 'testuser@gmail.com',
				'password': 'StronGPassworD2115'
			},
			headers={
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		)
		# Save auth token
		token = token_response.data.get('auth_token')
		# Set generated token as default authentication
		self.requestClient = APIClient()
		self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + token

	def testAddingProductToCart(self):
		pass
