from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import Invoiceserializer,InvoiceDetailserializer
from rest_framework.views import APIView



class InvoiceView(APIView):

    def get(self, request):
        queryset =invoice.objects.all()

        serializer = Invoiceserializer(queryset, many =True)
       

        return Response({
            'status' : True,
            'message' : 'Invoice fetched with GET',
            'data': serializer.data
        })

    def post(self, request,format=None):
        serializer = Invoiceserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailsView(APIView):
    
    def get(self, request, pk):
        try:
            queryset = invoiceDetail.objects.get(pk=pk)
           
            serializer = InvoiceDetailserializer(queryset)
           
            return Response({
            'status' : True,
            'message' : 'Invoice Details fetched with GET',
            'data': serializer.data,
           })
        except Exception as e:
            print(e)

            return Response({
                'status' : False,
                'message' : 'something went wrong',
                'data': serializer.data,
                
            })



    def post(self, request,format=None):
        
        serializer = InvoiceDetailserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 



# # Create your views here.
# class invoiceViewSet(viewsets.ModelViewSet):
#     query_set=invoice.objects.all()
#     serializer_class=Invoiceserializer

# @action(detail=True, methods=['post'])
# def invoice(self, request, pk=None):
#         invoice=invoice.objects.get()
#         serializer = Invoiceserializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)



# class invoiceDetailviewSet(viewsets.ModelViewSet):
#     queryset=invoiceDetail.objects.all()
#     serializer_class=InvoiceDetailserializer
#     def get_queryset(self):
#         return self.request.invoiceDetail.objects.all()




  

