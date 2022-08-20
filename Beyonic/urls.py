from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.customers,name='customers'),
    url(r'^$',views.companies,name = 'companies'),
]