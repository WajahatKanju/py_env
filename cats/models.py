from django.db import models
from django.core.validators import MinLengthValidator


class Breed(models.Model):
  name = models.CharField(max_length=200, validators=[MinLengthValidator(2)])


  def __str__(self):
    return self.name

class Cat(models.Model):
  nickname = models.CharField(
    max_length=200, validators=[MinLengthValidator(2)],
  )

  breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
  foods = models.CharField(max_length=300)
  weight = models.PositiveIntegerField()

  def __str__(self):
    return self.nickname