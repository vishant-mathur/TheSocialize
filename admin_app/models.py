from django.db import models
class Admin_signup(models.Model):
    Name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    class Meta:
        db_table='admin'
class CreateEvent(models.Model):

    # etype = (
    #   ('parties','PARTIES'),
    #   ('meetings','MEETINGS'),
    #   ('seminars','seminars'),
    #   )

    event_name=models.CharField(max_length=20)
    event_address=models.CharField(max_length=200)
    date_time=models.CharField(max_length=200)
    event_dis=models.CharField(max_length=300)
 
  
class Meta:
    db_table = 'events'
