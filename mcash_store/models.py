from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

class MCashTransaction(models.Model):
    customer_token = models.CharField(max_length=50)
    mcash_id = models.CharField(max_length=50, null=True, blank=True, default="")
    shopping_cart = models.ForeignKey('ShoppingCart', null=True)

class ShoppingCart(models.Model):
    STATUS_OPEN = 0
    STATUS_WAITING = 1
    STATUS_PAID = 2

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open cart'),
        (STATUS_WAITING, 'Waiting payment authorization'),
        (STATUS_PAID, 'Paid')
    )

    amount = models.FloatField(null=False, default=100.0)
    status = models.IntegerField(null=False, default=STATUS_OPEN, choices=STATUS_CHOICES)

    def to_dict(self):
        return {'id': self.id,
                'amount': self.amount,
                'status': self.status}
