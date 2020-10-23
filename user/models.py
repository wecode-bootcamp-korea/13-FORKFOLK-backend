from django.db      import models

class User(models.Model):
    email    = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
   
    class Meta:
        db_table = 'users'


