from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a Make(manufacturer) e.g Toyota',
            validators=[MinLengthValidator(2, 'Must be greater then one character')]
            )

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Must be greater then one character')]
        )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.nickname