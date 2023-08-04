import requests


class PaymentService:
    def __init__(self, payment_gateway_url):
        self.payment_gateway_url = payment_gateway_url

    def process_payment(self, payment):
        response = requests.post(
            self.payment_gateway_url,
            data={
                'order_id': payment.order_id,
                'amount': str(payment.amount)
            }
        )

        if response.status_code == 200:
            # if payment is successful, update the status
            payment.status = 'completed'
        else:
            # if payment failed, update the status
            payment.status = 'failed'

        payment.save()
