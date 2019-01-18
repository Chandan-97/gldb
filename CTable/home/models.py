from django.db import models

# Create your models here.

from django.conf import settings


class Campaign(models.Model):
    # Request_date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    request_date = models.DateField()
    campaign_name = models.CharField(max_length=100, default="Campaign Name")
    requester_name = models.CharField(max_length=100, default="Requester Name")
    campaign_email = models.CharField(max_length=100, default="Email@lge.com")
    # Campaign_end_date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    campaign_end_date = models.DateField()
    # Campaign_start_date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    campaign_start_date = models.DateField()

    def __str__(self):
        return "Campaign : " + self.Campaign_name

    class Meta:
        verbose_name_plural = "Campaign"
