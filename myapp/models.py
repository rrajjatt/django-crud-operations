from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    salary = models.IntegerField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.fname
