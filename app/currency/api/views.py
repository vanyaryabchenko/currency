from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import filters as rest_framework_filters

from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.filters import RateFilter, ContactUsFilter
from currency.models import Rate, Source, ContactUs
from currency.paginators import RatesSetPagination


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = RatesSetPagination
    filter_backends = (filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter)
    filterset_class = RateFilter
    ordering_fields = ('id', 'created', 'buy', 'sale')


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter
    )
    filterset_class = ContactUsFilter
    ordering_fields = ('id', 'email_from')
    search_fields = ['id', 'email_from', 'subject']
