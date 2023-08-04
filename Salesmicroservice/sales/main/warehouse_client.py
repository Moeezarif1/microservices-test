import requests


class WarehouseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_product_details(self, product_id):
        response = requests.get(f'{self.base_url}/product/{product_id}/retrieve_product/')

        if response.status_code == 200:
            product = response.json()
            print(product)
            return {'product_quantity': product['product_quantity'], 'product_price': product['product_price']}

        elif response.status_code == 404:
            raise Exception('Product not found')

        else:
            raise Exception('Error contacting Warehouse microservice')

    def update_product_quantity(self, product_id, new_quantity):
        response = requests.patch(f'{self.base_url}/product/{product_id}/',
                                  json={'product_quantity': new_quantity})
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()