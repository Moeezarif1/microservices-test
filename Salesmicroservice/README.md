# Sales Microservice
This service handles the creation and management of sales orders for the test_task application.

## Table of Contents
1. [Description](#description)
2. [Models](#models)
3. [API Client](#api-client)
4. [Environment Variables](#environment-variables)
5. [Running the Service Locally](#running-locally)
6. [Running the Service in Docker](#running-docker)
7. [Resources](#resources)

## Description <a name="description"/>
The Sales Microservice is a Django application which provides a REST API interface for creating and managing sales orders. It communicates with the Warehouse Microservice to check the availability of products and to update their quantity in the warehouse after an order is placed.

## Models <a name="models"/>
This microservice includes the following models:
- **Order**: Represents a sales order. It has fields for `product_id` (represented as a UUID), `quantity`, and `price`. When an `Order` instance is saved, it communicates with the `WarehouseAPI` to check product availability and calculate the total price.

## API Client <a name="api-client"/>
- **WarehouseAPI**: This class is a client for the Warehouse Microservice API. It communicates with the Warehouse Microservice to get product details (`get_product_details` method) and to update the product quantity (`update_product_quantity` method).


## Credentials <a name="credentials"/>

Superuser for Django:
- Username: django
- Password: django

User for the local postgres db:
```shell
CREATE USER neednect_user WITH PASSWORD 'password';
```


## Environment Variables <a name="environment-variables"/>
This microservice uses the following environment variables:
- `POSTGRES_USER`
- `POSTGRES_NAME`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`

## Running the Service Locally <a name="running-locally"/>
To run the service locally, you will need Python and Django installed. 

1. Clone the repository
2. Create a virtual environment using `python -m venv venv`
3. Activate the virtual environment using `source venv/bin/activate`
4. Install dependencies using `pip install -r requirements.txt`
5. Run the service using `python manage.py runserver`

## Running the Service in Docker <a name="running-docker"/>
To run the service in a Docker container, you will need Docker and Docker Compose installed.

1. Clone the repository
2. Run `docker-compose build sales` from the root directory
3. Run `docker-compose up` from the root directory

## Resources <a name="resources"/>
1. Django Rest Framework https://www.django-rest-framework.org/
2. Django Documentation https://docs.djangoproject.com/
3. Docker Documentation https://docs.docker.com/

## Tests
Tests can be run using Django's built-in test command: `python manage.py test`.

**Note**: The Sales Microservice must be able to communicate with the Warehouse Microservice for the order validation and creation logic to work correctly. Ensure that the Warehouse Microservice is running and is accessible from the Sales Microservice.