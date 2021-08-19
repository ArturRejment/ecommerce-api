# ecommerce-api
API for ecommerce

## Run server with Docker

- Clone this repo
- In terminal hit `docker-compose run shopserver`
- Close running process with `Ctrl + C`
- Run server with `docker-compose up`
- Open new terminal
- Go to the server container with `docker exec -it shopserver bash`
- Migrate database with `python manage.py migrate`
- And create superuser with `python manage.py createsuperuser`

## Endpoints

### /product/list/
- `GET` Returns all products paginated for 12 products per site

### /product/\<int:id>/
- `GET` Returns specific product

### /cart/
- `GET` Obtain current state of the cart. Contains total value, number of products in the cart and all products

### /cart/cartitem/\<int:id>/
- `POST` Add product specified by id to the cart
- `DELETE` Remove product specified by id from the cart

## Authentication

### /auth/users/
- `POST` Allows to register new user with:
  - email
  - password
  - re_password
  - first_name
  - last_name
  - phone

### /auth/token/login/
- `POST` Allows to login user with email and password

### /auth/token/logout/
- `POST` Allows to logout user
