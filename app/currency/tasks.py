from celery import shared_task
from django.conf import settings
import requests
from currency.choices import RateCurrencyChoices
from currency.constants import PRIVATBANK_CODE_NAME
from currency.utils import to_2_point_decimal


@shared_task
def parse_privatbank():

    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()

    if source is None:
        source = Source.objects.create(name=PRIVATBANK_CODE_NAME, code_name=PRIVATBANK_CODE_NAME, source_url=url)

    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue
        buy = to_2_point_decimal(rate['buy'])
        sale = to_2_point_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        )\
            .order_by('created')\
            .last()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
