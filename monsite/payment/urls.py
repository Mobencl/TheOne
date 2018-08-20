from django.conf.urls import url
from django.conf import settings

app_name = 'Payment

urlpatterns = [
        url(r'^paypal/',include('paypal.standard.ipn.urls'))
]
