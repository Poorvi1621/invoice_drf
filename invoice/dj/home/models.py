from django.db import models

class invoice(models.Model):
    date=models.DateField(auto_now_add=True)
    invoice_no=models.CharField(max_length=20,null=True, blank=True)
    cust_name=models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
         return self.cust_name


class invoiceDetail(models.Model):
    invoice=models.ForeignKey(invoice,on_delete=models.CASCADE,null=True, blank=True)
    desc=models.TextField()
    qty=models.IntegerField()
    unitprice=models.CharField(max_length=20,null=True, blank=True)
    price=models.CharField(max_length=20,null=True, blank=True)
    def __str__(self):
        return f'{self.invoice.invoice_no}'



