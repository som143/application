from django.db import models
from django.contrib.auth.models import User

class reg(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.username
class api(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    class Meta:
        managed = "False"
        db_table = "api"
