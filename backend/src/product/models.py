from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    name = models.CharField(max_length=100, unique=True)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)

    def __str__(self):
        return self.name