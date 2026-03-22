from django.db import models

# Create your models here.
# from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.username