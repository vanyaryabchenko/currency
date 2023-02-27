from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.forms import SourceForm
from currency.models import Rate, ContactUs, Source


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


def template_source(request):
    source = Source.objects.all()
    context = {
        'source': source
    }
    return render(request, 'source_table.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/template/source')
    elif request.method == 'GET':
        form = SourceForm()
    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/template/source')
    elif request.method == 'GET':
        form = SourceForm(instance=source)
    context = {
        'form': form
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/template/source')
    elif request.method == 'GET':
        context = {
            'source': source
        }
    return render(request, 'source_delete.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)
    context = {
        'source': source
    }
    return render(request, 'source_details.html', context)
