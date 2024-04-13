from django.db import models



class accounts(models.Model):
    username = models.CharField(max_length=20)
    
    pass