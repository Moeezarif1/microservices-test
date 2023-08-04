import requests


class SalesAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def update_order_status(self, order_id, status):
        response = requests.post(
            f'{self.base_url}/order/update',
            json={
                'order_id': order_id,
                'status': status
            }
        )

        if response.status_code != 200:
            # handle error - maybe raise an exception, or retry the request
            raise Exception('Failed to update order status in Sales service')
