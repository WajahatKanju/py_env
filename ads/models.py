from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Ad(models.Model):
  title = models.CharField(max_length=200, validators=[MinLengthValidator(2, 'ad title must be greater than 2 characters')])
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
  text = models.TextField() 

  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  crearted_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title