from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.files.storage import default_storage

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def filter_model(request, o, s):
    if request.method == 'POST':
        data = request.data
        if isinstance(data, list):
            # multiple entries
            queryset = o.objects.all()
            for item in data:
                column_name = item.get('columnName')
                column_key = item.get('columnKey')
                if column_name and column_key:
                    queryset = queryset.filter(**{column_name: column_key})
                else:
                    return JsonResponse({'error': 'Invalid input data.'}, status=400)
            serializer = s(queryset, many=True)  # Replace YourSerializerClass with the actual serializer class
            response_data = serializer.data
        else:
            # single entry
            column_name = data.get('columnName')
            column_key = data.get('columnKey')
            if column_name and column_key:
                queryset = o.objects.filter(**{column_name: column_key})
                serializer = s(queryset, many=True)  # Replace YourSerializerClass with the actual serializer class
                response_data = serializer.data
            else:
                return JsonResponse({'error': 'Invalid input data.'}, status=400)
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def generic_list(request, o, s, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            ds = s(dt)
            return Response(ds.data)
        else:
            dt = o.objects.all()

            ds = s(dt, many=True)
            return Response(ds.data)

    elif request.method == 'POST':
        ds = s(data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data, status=status.HTTP_201_CREATED)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            dt = o.objects.get(id=pk)
        except o.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ds = s(dt, data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def generic_delete(request, o, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            dt.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def PeopleSupplier_list(request, pk=None):
    return generic_list(request, PeopleSupplier, PeopleSupplierSerializer, pk)

@csrf_exempt
def PeopleSupplier_filter(request):
    return filter_model(request, PeopleSupplier, PeopleSupplierSerializer)

@csrf_exempt
def PeopleSupplier_delete(request, pk=None):
    return generic_delete(request, PeopleSupplier, pk)


@csrf_exempt
def PeopleCustomer_list(request, pk=None):
    return generic_list(request, PeopleCustomer, PeopleCustomerSerializer, pk)

@csrf_exempt
def PeopleCustomer_filter(request):
    return filter_model(request, PeopleCustomer, PeopleCustomerSerializer)

@csrf_exempt
def PeopleCustomer_delete(request, pk=None):
    return generic_delete(request, PeopleCustomer, pk)


@csrf_exempt
def SalesOrder_list(request, pk=None):
    return generic_list(request, SalesOrder, SalesOrderSerializer, pk)

@csrf_exempt
def SalesOrder_filter(request):
    return filter_model(request, SalesOrder, SalesOrderSerializer)

@csrf_exempt
def SalesOrder_delete(request, pk=None):
    return generic_delete(request, SalesOrder, pk)


@csrf_exempt
def SalesItems_list(request, pk=None):
    return generic_list(request, SalesItems, SalesItemsSerializer, pk)

@csrf_exempt
def SalesItems_filter(request):
    return filter_model(request, SalesItems, SalesItemsSerializer)

@csrf_exempt
def SalesItems_delete(request, pk=None):
    return generic_delete(request, SalesItems, pk)


@csrf_exempt
def SalesTransaction_list(request, pk=None):
    return generic_list(request, SalesTransaction, SalesTransactionsSerializer, pk)

@csrf_exempt
def SalesTransaction_filter(request):
    return filter_model(request, SalesTransaction, SalesTransactionsSerializer)

@csrf_exempt
def SalesTransaction_delete(request, pk=None):
    return generic_delete(request, SalesTransaction, pk)

@csrf_exempt
def PurchaseOrder_list(request, pk=None):
    return generic_list(request, PurchaseOrder, PurchaseOrderSerializer, pk)

@csrf_exempt
def PurchaseOrder_filter(request):
    return filter_model(request, PurchaseOrder, PurchaseOrderSerializer)

@csrf_exempt
def PurchaseOrder_delete(request, pk=None):
    return generic_delete(request, PurchaseOrder, pk)


@csrf_exempt
def PurchaseItems_list(request, pk=None):
    return generic_list(request, PurchaseItems, PurchaseItemsSerializer, pk)

@csrf_exempt
def PurchaseItems_filter(request):
    return filter_model(request, PurchaseItems, PurchaseItemsSerializer)

@csrf_exempt
def PurchaseItems_delete(request, pk=None):
    return generic_delete(request, PurchaseItems, pk)


@csrf_exempt
def PurchaseTransaction_list(request, pk=None):
    return generic_list(request, PurchaseTransaction, PurchaseTransactionsSerializer, pk)

@csrf_exempt
def PurchaseTransaction_filter(request):
    return filter_model(request, PurchaseTransaction, PurchaseTransactionsSerializer)

@csrf_exempt
def PurchaseTransaction_delete(request, pk=None):
    return generic_delete(request, PurchaseTransaction, pk)


@csrf_exempt
def ProductItem_list(request, pk=None):
    return generic_list(request, ProductItem, ProductItemSerializer, pk)

@csrf_exempt
def ProductItem_filter(request):
    return filter_model(request, ProductItem, ProductItemSerializer)

@csrf_exempt
def ProductItem_delete(request, pk=None):
    return generic_delete(request, ProductItem, pk)



@csrf_exempt
def ProductCategory_list(request, pk=None):
    return generic_list(request, ProductCategory, ProductCategorySerializer, pk)

@csrf_exempt
def ProductCategory_filter(request):
    return filter_model(request, ProductCategory, ProductCategorySerializer)

@csrf_exempt
def ProductCategory_delete(request, pk=None):
    return generic_delete(request, ProductCategory, pk)



@csrf_exempt
def ProductSubCategory_list(request, pk=None):
    return generic_list(request, ProductSubCategory, ProductSubCategorySerializer, pk)

@csrf_exempt
def ProductSubCategory_filter(request):
    return filter_model(request, ProductSubCategory, ProductSubCategorySerializer)

@csrf_exempt
def ProductSubCategory_delete(request, pk=None):
    return generic_delete(request, ProductSubCategory, pk)



@csrf_exempt
def ProductBrand_list(request, pk=None):
    return generic_list(request, ProductBrand, ProductBrandSerializer, pk)

@csrf_exempt
def ProductBrand_filter(request):
    return filter_model(request, ProductBrand, ProductBrandSerializer)

@csrf_exempt
def ProductBrand_delete(request, pk=None):
    return generic_delete(request, ProductBrand, pk)