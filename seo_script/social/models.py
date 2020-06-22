from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    business = models.CharField(max_length=100)

    def __str__(self):
        return self.email
