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
