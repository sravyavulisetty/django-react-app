# models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.EmailField()
    contact = models.CharField(max_length=15)
    access = models.CharField(max_length=10)

    def _str_(self):
        return self.name