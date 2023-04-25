from django.urls import path
from rest_framework.routers import DefaultRouter

from currency.api.views import RateViewSet, SourceListView, ContactUsViewSet

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'contactus', ContactUsViewSet, basename='contactUs')
urlpatterns = [
    path('source/', SourceListView.as_view(), name='source-list')
]

urlpatterns += router.urls
