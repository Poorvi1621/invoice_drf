from rest_framework import serializers
from .models import *

class Invoiceserializer(serializers.ModelSerializer):
        
    class Meta:
        model = invoice
        fields='__all__'

class InvoiceDetailserializer(serializers.ModelSerializer):
    invoice = Invoiceserializer()
    class Meta:
        model = invoiceDetail
        fields = ['invoice','desc','qty','unitprice','price']
