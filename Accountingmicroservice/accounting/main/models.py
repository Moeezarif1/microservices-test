from django.db import models


# Create your models here.


class Payment(models.Model):
    order_id = models.CharField(max_length=36)  # Assuming order_id is UUID saved as a CharField
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)  # could be 'completed', 'pending', 'failed', etc.
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'accounting_payments'
