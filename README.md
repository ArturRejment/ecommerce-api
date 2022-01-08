# ecommerce-api
API for ecommerce

# 1. Run server with Docker

- Clone this repo
- In terminal hit `docker-compose run shopserver`
- Close running process with `Ctrl + C`
- Run server with `docker-compose up`
- Open new terminal
- Go to the server container with `docker exec -it shopserver bash`
- Migrate database with `python manage.py migrate`
- And create superuser with `python manage.py createsuperuser`

# 2. Endpoints

## 2.1 Products

### 2.1.1 /product/get-all/
- `GET` Returns all products
```json
[
    {
        "id": 3,
        "product_name": "Airpods Pro",
        "retail_price_brutt": 1537.49875,
        "stock_status": 10,
        "stock_availability": 5,
        "categories": [
            "elektronika"
        ],
        "image_url": "http://127.0.0.1:8000/static/images/product_pictures/kwiat.png"
    },
    {
        "id": 2,
        "product_name": "Ciasta",
        "retail_price_brutt": 18.45,
        "stock_status": 20,
        "stock_availability": 180,
        "categories": [
            "artykuly-spozywcze"
        ],
        "image_url": "http://127.0.0.1:8000/static/images/product_pictures/test-1_2.png"
    },
    {
        "id": 1,
        "product_name": "Maszynka Do Golenia",
        "retail_price_brutt": 270.6,
        "stock_status": 20,
        "stock_availability": 15,
        "categories": [
            "produkty-domowe"
        ],
        "image_url": "http://127.0.0.1:8000/static/images/default.jpg"
    }
]
```

### 2.1.2 /product/\<int:id>/get/
- `GET` Returns details about product specified by id
```json
{
    "id": 3,
    "product_name": "Airpods Pro",
    "detail_description": "re the only in-ear headphones with Active Noise Cancellation that continuously adapts to the geometry of your ear and the fit of the ear tips — blocking out the world so you can focus on what you're listening to. An outward-facing microphone detects external sound.",
    "stock_status": 10,
    "retail_price_brutt": 1537.49875,
    "whole_price_brutt": 1291.49895,
    "tax": "22.9999",
    "is_visible": false,
    "is_new": true,
    "accession_number": "FFI55",
    "shipping_cost": "15.00",
    "categories": [
        "elektronika"
    ],
    "tags": [
        "sluchawki"
    ],
    "seasons": [
        "caloroczne"
    ]
}
```

## 2.2 Cart

### 2.2.1 /cart/get/
- `GET` Returns cart for user identified with Authorization header
```json
{
    "id": 3,
    "user": 4,
    "get_products_quantity": 1,
    "get_cart_total": 1537.49875,
    "products": [
        {
            "id": 6,
            "product": {
                "id": 3,
                "product_name": "Airpods Pro",
                "retail_price_brutt": 1537.49875,
                "image_url": "http://127.0.0.1:8000/static/images/product_pictures/kwiat.png"
            },
            "quantity": 1
        }
    ]
}
```

### 2.2.2 /cart/<int:id>/add/
- `POST` Adds product specified by id to users cart

### 2.2.2 /cart/<int:id>/remove/
- `POST` Removes product specified by id from users cart

## 2.3 Order

### 2.3.1 /order/create/
- `POST` create order from users cart
```json
{
    "total_cost_net": "1537.4988",
    "discount_code": null,
    "status": 0,
    "cart": {
        "id": 3,
        "user": 4,
        "get_products_quantity": 1,
        "get_cart_total": 1537.49875,
        "products": [
            {
                "id": 6,
                "product": {
                    "id": 3,
                    "product_name": "Airpods Pro",
                    "retail_price_brutt": 1537.49875,
                    "image_url": "http://127.0.0.1:8000/static/images/product_pictures/kwiat.png"
                },
                "quantity": 1
            }
        ]
    },
    "user": 4
}
```

## 2.4 Authentication

### 2.4.1 /auth/users/
- `POST` Allows to register new user with:
  - email
  - password
  - re_password
  - first_name
  - last_name
  - phone

### 2.4.2 /auth/token/login/
- `POST` Allows to login user with email and password
```json
{
    "auth_token": "1dd9e42eb09b30d7f2ed3302db5aa68d9453e998"
}
```

### 2.4.3 /auth/token/logout/
- `POST` Allows to logout user
