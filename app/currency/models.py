from django.db import models
from django.templatetags.static import static

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(choices=RateCurrencyChoices.choices)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}, Sale:{self.sale}'


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()


def source_image_path(instance, filename):
    return f'source/{instance.id}/{filename}'


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)
    image = models.FileField(default=None, null=True, blank=True, upload_to=source_image_path)

    def __str__(self):
        return f'{self.name}'

    @property
    def source_image_url(self):
        if self.image:
            return self.image.url
        return static('av.png')


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=128)
    request_method = models.CharField(max_length=4)
    time = models.PositiveIntegerField()
