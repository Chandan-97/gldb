from django.db import models

# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=30, default="TESTNAME")
    email = models.CharField(max_length=40, default="TEST@GMAIL.COM")
    phoneno = models.IntegerField(default=1)

    def __str__(self):
        return "Profile : " + self.name

class Product (models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    modelno = models.CharField(max_length=10, primary_key = True, default="MODELNO")
    price = models.CharField(max_length=10, default="10")
    warranty = models.CharField(max_length=10, default="WARRANTY")

    def __str__(self):
        return "Product : " + self.modelno

class Service (models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    log_date = models.DateField()
    total_cost = models.IntegerField(default=10)

    def __str__(self):
        return "Service : " + self.model.modelno

class ProductHierarchy (models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length = 100, default="CATEGORY")
    group = models.CharField(max_length = 100, default="GROUP")

    def __str__(self):
        return "ProductHierarchy : " + self.model.modelno

class ProfileExtension (models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    sms = models.BooleanField(default = True)
    email = models.BooleanField(default = True)

    def __str__(self):
        return "ProfileExtension : " + self.user.name