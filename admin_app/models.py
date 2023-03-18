from django.db import models
class Admin_signup(models.Model):
    Name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    class Meta:
        db_table='admin'
