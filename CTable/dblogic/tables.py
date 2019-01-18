from django.db import models

# Create your models here.


class CustomerProfile (models.Model):
    customer_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30, default="TESTNAME")
    phoneno = models.IntegerField(default=-1)
    cellular_no = models.IntegerField(default=-1)
    email_addr = models.CharField(max_length=40, default="LGIN@GMAIL.COM")
    address_line1_info = models.CharField(max_length=50, default="N/A")
    address_line2_info = models.CharField(max_length=50, default="N/A")
    address_line3_info = models.CharField(max_length=50, default="N/A")
    city_name = models.CharField(max_length=20, default="N/A")
    state_name = models.CharField(max_length=20, default="N/A")
    postal_code = models.IntegerField(max_length=10, default=-1)

    class Meta:
        verbose_name_plural = "CustomerProfile"

    def __str__(self):
        return "Customer : " + self.customer_no

class Product (models.Model):
    product_id = models.AutoField(primary_key=True)
    model_code = models.CharField(max_length=30, default="N/A")
    active_status = models.BooleanField(default=False)
    product1_code = models.CharField(max_length=15, default="N/A")
    product2_code = models.CharField(max_length=15, default="N/A")
    product3_code = models.CharField(max_length=15, default="N/A")
    product4_code = models.CharField(max_length=15, default="N/A")
    specification_desc = models.CharField(max_length=100, default="N/A")

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return "Product : " + self.product_id

