from django.shortcuts import render

from rest_framework import viewsets

from .models import QuoteItem
from .serializers import QuoteItemSerializer



class DataListView(viewsets.ModelViewSet):
    queryset = QuoteItem.objects.all()
    serializer_class = QuoteItemSerializer