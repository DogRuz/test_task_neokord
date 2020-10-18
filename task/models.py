from django.db import models

# Create your models here.
class Number(models.Model):
    get_number = models.IntegerField(verbose_name='Number')
    fibonacci_number = models.IntegerField(null=True, blank=True, verbose_name='Number fibonacci')