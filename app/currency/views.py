from django.http import HttpResponse
from django.shortcuts import render
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


def template_rates(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rates_table.html', context)


def template_contactus(request):
    contactus = ContactUs.objects.all()
    context = {
        'contactus': contactus
    }
    return render(request, 'contactus_table.html', context)
