from rest_framework.routers import DefaultRouter

from currency.api.views import RateViewSet, SourceViewSet, ContactUsViewSet

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'contactus', ContactUsViewSet, basename='contactUs')
router.register(r'source', SourceViewSet, basename='source')
urlpatterns = []

urlpatterns += router.urls
