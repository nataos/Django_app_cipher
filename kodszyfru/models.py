from django.db import models

# Create your models here.
class Passwords(models.Model):
    text = models.TextField(max_length=20000,null=True)
    cipher = models.TextField(max_length=20000)

    def __str__(self):
        return f'{self.text}{self.cipher}'

