from django.db import models

# Create your models here.

from django.conf import settings

from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model

User = get_user_model()

class Campaign(models.Model):
    campaign_name = models.CharField(max_length=100, default="Campaign Name")
    requester_name = models.CharField(max_length=100, default="Requester Name")
    request_date = models.DateField()
    campaign_start_date = models.DateField()
    campaign_end_date = models.DateField()
    campaign_email = models.CharField(max_length=100, default="Email@lge.com")

    def __str__(self):
        return "Campaign : " + self.campaign_name

    class Meta:
        verbose_name_plural = "Campaign"

class Product(models.Model):
    product_name = models.CharField(max_length=20, default="N/A")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Product"

class TextFile(models.Model):
    result = models.FileField(null=True, blank=True)
    query = models.CharField(max_length=1000)
    file_name = models.CharField(max_length=200, default="NA")

