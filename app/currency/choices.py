from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'EUR'
    USD = 2, 'USD'
