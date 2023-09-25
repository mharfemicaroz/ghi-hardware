from rest_framework import serializers
from .models import *

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class ProductSubCategorySerializer(serializers.ModelSerializer):
    category_data = ProductCategorySerializer(source='category', read_only=True)
    class Meta:
        model = ProductSubCategory
        fields = '__all__'

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'

class PeopleSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleSupplier
        fields = '__all__'

class ProductItemSerializer(serializers.ModelSerializer):
    category_data = ProductCategorySerializer(source='category', read_only=True)
    subcategory_data = ProductSubCategorySerializer(source='subcategory', read_only=True)
    brand_data = ProductBrandSerializer(source='brand', read_only=True)
    class Meta:
        model = ProductItem
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier_data = PeopleSupplierSerializer(source='supplier', read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseItemsSerializer(serializers.ModelSerializer):
    product_data = ProductItemSerializer(source='product', read_only=True)
    purchaseOrder_data = PurchaseOrderSerializer(source='purchaseOrder', read_only=True)
    class Meta:
        model = PurchaseItems
        fields = '__all__'

class PurchaseTransactionsSerializer(serializers.ModelSerializer):
    purchaseOrder_data = PurchaseOrderSerializer(source='purchaseOrder', read_only=True)
    class Meta:
        model = PurchaseTransaction
        fields = '__all__'
