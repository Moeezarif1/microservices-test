import requests


class AccountingAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_payment(self, order_id, amount):
        response = requests.post(f'{self.base_url}/payments/', json={
            'order_id': order_id,
            'amount': amount,
        })

        if response.status_code == 201:
            return response.json()

        elif response.status_code == 404:
            raise Exception('Order not found')

        else:
            raise Exception('Error contacting Accounting microservice')

    def get_payment_status(self, payment_id):
        response = requests.get(f'{self.base_url}/payments/{payment_id}/')

        if response.status_code == 200:
            payment = response.json()
            return payment['status']

        elif response.status_code == 404:
            raise Exception('Payment not found')

        else:
            raise Exception('Error contacting Accounting microservice')

    def update_payment_status(self, payment_id, status):
        response = requests.patch(f'{self.base_url}/payments/{payment_id}/', json={
            'status': status,
        })

        if response.status_code == 200:
            return response.json()

        response.raise_for_status()
