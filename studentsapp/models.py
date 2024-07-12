from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.secondname}"


