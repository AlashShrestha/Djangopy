from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=300, default="This is Sub Heading")
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
