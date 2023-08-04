import requests


def orderValidationandPricing(itemId):
    response = requests.get(f'http://warehouse:8000/api/product/{itemId}/retrieve_product/')
    print(response.request.url)
    print(response.status_code)
    if response.status_code == 200:

        product = response.json()
        print(product)
        return product['product_quantity'], product['product_price']
    elif response.status_code == 404:
        raise Exception('Product not found')
    else:
        raise Exception('Error contacting Warehouse microservice')
