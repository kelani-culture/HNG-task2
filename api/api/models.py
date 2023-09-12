from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50,
                            help_text="User name")