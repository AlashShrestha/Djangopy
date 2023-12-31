from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    sub_heading = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Links(models.Model):
    url = models.URLField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.icon


class CompanyName(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
