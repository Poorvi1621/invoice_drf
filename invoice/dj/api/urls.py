
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from home.views import *


urlpatterns = [
    path('invoice/', InvoiceView.as_view()),
    path('invoice-detail/<pk>', InvoiceDetailsView.as_view()),
    
    
   

]

# router = routers.DefaultRouter()
# router.register(r'invoice', views.invoiceViewSet ,basename='invoice')
# router.register(r'invoiceDetail', views.invoiceDetailviewSet ,basename='invoiceDetail')

# # Wire up our API using automatic URL routing.

# urlpatterns = [
#     path('', include(router.urls)),
    
# ]