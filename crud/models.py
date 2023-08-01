from django.db import models


# Create your models here.
class Blog(models.Model):
    user_name = models.CharField(max_length=150)
    title = models.CharField(max_length=300)
    sub_heading = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.user_name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
