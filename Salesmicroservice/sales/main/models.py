from django.db import models, transaction
from django.core.validators import MinValueValidator
from .queries import orderValidationandPricing
from .warehouse_client import WarehouseAPI


# Create your models here.
class Order(models.Model):
    product_id = models.CharField(null=True, max_length=36)  # UUID as a CharField
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(null=True, editable=False)

    # new status field
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table = 'sales_orders'

    @transaction.atomic
    def save(self, *args, **kwargs):
        warehouse_api = WarehouseAPI('http://warehouse:8000/api')
        product_details = warehouse_api.get_product_details(self.product_id)
        product_quantity, product_price = product_details['product_quantity'], product_details['product_price']

        if product_quantity >= self.quantity:
            self.price = product_price * self.quantity
            # Update the product quantity in the warehouse
            warehouse_api.update_product_quantity(self.product_id, product_quantity - self.quantity)
            super(Order, self).save(*args, **kwargs)
        else:
            raise Exception("Insufficient Quantity available")

