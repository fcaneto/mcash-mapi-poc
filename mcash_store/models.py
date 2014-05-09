from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

class MCashTransaction(models.Model):
    customer_token = models.CharField(max_length=50)
    session_id = models.CharField(max_length=50, null=True, blank=True, default="")
    mcash_id = models.CharField(max_length=50, null=True, blank=True, default="")
