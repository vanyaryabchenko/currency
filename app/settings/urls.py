"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from currency.views import list_rates, list_contactus, template_rates, template_contactus, template_source, \
    source_create, source_update, source_delete, source_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('contactus/list', list_contactus),
    path('template/rates', template_rates),
    path('template/contactus', template_contactus),
    path('template/source', template_source),
    path('source/create', source_create),
    path('source/update/<int:pk>', source_update),
    path('source/delete/<int:pk>', source_delete),
    path('source/details/<int:pk>', source_details),
]
