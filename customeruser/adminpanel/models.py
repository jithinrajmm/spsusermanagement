from pyexpat import model
from unittest import defaultTestLoader
from django.db import models

# Create your models here.

class Admin(models.Model):

    admin_name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    is_logedin = models.BooleanField(default=False)

    @property
    def loginornot(self):
        return self.is_logedin


    def admin_authenticate(self,name,password):
        if self.admin_name == name and self.password == password:
            self.is_logedin = True
            return True
        else:
            return False

    def admin_logout(self):
        self.is_logedin = False
    
    def __str__(self):
        return self.admin_name




