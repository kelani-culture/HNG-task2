from django.db import models
from .utils import generate_id

class User(models.Model):
    id = models.CharField(max_length=4, unique=True, primary_key=True,\
                          default=generate_id)
    name = models.CharField(max_length=50,
                            help_text="User name")
    
    def __str__(self):
        return self.name