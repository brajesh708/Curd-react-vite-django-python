from django.db import models

# Create your models here.

class EmployeData(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    selary=models.IntegerField(max_length=50)
    
    def __str__(self):
        return self.name
                             
                             