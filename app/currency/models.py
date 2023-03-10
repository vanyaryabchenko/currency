from django.db import models

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(choices=RateCurrencyChoices.choices)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}, Sell:{self.sell}'


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'SOURCE URL: {self.source_url}    NAME: {self.name}'


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=128)
    request_method = models.CharField(max_length=4)
    time = models.PositiveIntegerField()
