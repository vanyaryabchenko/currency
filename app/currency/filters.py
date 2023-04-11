import django_filters
from currency.models import Rate, Source, ContactUs


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale']


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', ]


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['email_from', ]
