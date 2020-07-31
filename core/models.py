from django.db import models


# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=False)
    concerntype= models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name
