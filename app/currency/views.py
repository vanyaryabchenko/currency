from django.http import HttpResponse

from currency.models import Rate, ContactUs
# Create your views here.


def list_rates(request):
    qs = Rate.objects.all()
    result = []
    for rate in qs:
        result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, '
                      f'currency: {rate.currency}, created: {rate.created}<br>')
    return HttpResponse(str(result))


def list_contactus(request):
    qs = ContactUs.objects.all()
    result = []
    for contactus in qs:
        result.append(f'id: {contactus.id}, email: {contactus.email_from}, '
                      f'subject: {contactus.subject}, message: {contactus.message}<br>')
    return HttpResponse(str(result))
