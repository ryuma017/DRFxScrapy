import requests

from django.urls import reverse_lazy
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'browse/index.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        domain = 'http://127.0.0.1:8000'
        datalist_url = domain + reverse_lazy('apiapp:data-list')

        response = requests.get(datalist_url)
        quotedata = response.json()

        return quotedata
