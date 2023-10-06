from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [

    re_path(r'^people/supplier/$', PeopleSupplier_list, name='PeopleSupplier-list'),
    re_path(r'^people/supplier/(?P<pk>\d+)/$', PeopleSupplier_list, name='PeopleSupplier-detail'),
    re_path(r'^people/supplier/filter/$', PeopleSupplier_filter, name='PeopleSupplier-filter'),
    re_path(r'^people/supplier/delete/(?P<pk>\d+)/$', PeopleSupplier_delete, name='PeopleSupplier-delete'),

    re_path(r'^people/customer/$', PeopleCustomer_list, name='PeopleCustomer-list'),
    re_path(r'^people/customer/(?P<pk>\d+)/$', PeopleCustomer_list, name='PeopleCustomer-detail'),
    re_path(r'^people/customer/filter/$', PeopleCustomer_filter, name='PeopleCustomer-filter'),
    re_path(r'^people/customer/delete/(?P<pk>\d+)/$', PeopleCustomer_delete, name='PeopleCustomer-delete'),

    re_path(r'^sales/order/$', SalesOrder_list, name='SalesOrder-list'),
    re_path(r'^sales/order/(?P<pk>\d+)/$', SalesOrder_list, name='SalesOrder-detail'),
    re_path(r'^sales/order/filter/$', SalesOrder_filter, name='SalesOrder-filter'),
    re_path(r'^sales/order/delete/(?P<pk>\d+)/$', SalesOrder_delete, name='SalesOrder-delete'),
    
    re_path(r'^sales/items/$', SalesItems_list, name='SalesItems-list'),
    re_path(r'^sales/items/(?P<pk>\d+)/$', SalesItems_list, name='SalesItems-detail'),
    re_path(r'^sales/items/filter/$', SalesItems_filter, name='SalesItems-filter'),
    re_path(r'^sales/items/delete/(?P<pk>\d+)/$', SalesItems_delete, name='SalesItems-delete'),

    re_path(r'^sales/transact/$', SalesTransaction_list, name='SalesTransaction-list'),
    re_path(r'^sales/transact/(?P<pk>\d+)/$', SalesTransaction_list, name='SalesTransaction-detail'),
    re_path(r'^sales/transact/filter/$', SalesTransaction_filter, name='SalesTransaction-filter'),
    re_path(r'^sales/transact/delete/(?P<pk>\d+)/$', SalesTransaction_delete, name='SalesTransaction-delete'),

    re_path(r'^purchase/order/$', PurchaseOrder_list, name='PurchaseOrder-list'),
    re_path(r'^purchase/order/(?P<pk>\d+)/$', PurchaseOrder_list, name='PurchaseOrder-detail'),
    re_path(r'^purchase/order/filter/$', PurchaseOrder_filter, name='PurchaseOrder-filter'),
    re_path(r'^purchase/order/delete/(?P<pk>\d+)/$', PurchaseOrder_delete, name='PurchaseOrder-delete'),
    
    re_path(r'^purchase/items/$', PurchaseItems_list, name='PurchaseItems-list'),
    re_path(r'^purchase/items/(?P<pk>\d+)/$', PurchaseItems_list, name='PurchaseItems-detail'),
    re_path(r'^purchase/items/filter/$', PurchaseItems_filter, name='PurchaseItems-filter'),
    re_path(r'^purchase/items/delete/(?P<pk>\d+)/$', PurchaseItems_delete, name='PurchaseItems-delete'),

    re_path(r'^purchase/transact/$', PurchaseTransaction_list, name='PurchaseTransaction-list'),
    re_path(r'^purchase/transact/(?P<pk>\d+)/$', PurchaseTransaction_list, name='PurchaseTransaction-detail'),
    re_path(r'^purchase/transact/filter/$', PurchaseTransaction_filter, name='PurchaseTransaction-filter'),
    re_path(r'^purchase/transact/delete/(?P<pk>\d+)/$', PurchaseTransaction_delete, name='PurchaseTransaction-delete'),

    re_path(r'^product/category/$', ProductCategory_list, name='ProductCategory-list'),
    re_path(r'^product/category/(?P<pk>\d+)/$', ProductCategory_list, name='ProductCategory-detail'),
    re_path(r'^product/category/filter/$', ProductCategory_filter, name='ProductCategory-filter'),
    re_path(r'^product/category/delete/(?P<pk>\d+)/$', ProductCategory_delete, name='ProductCategory-delete'),
    
    re_path(r'^product/category/sub/$', ProductSubCategory_list, name='ProductSubCategory-list'),
    re_path(r'^product/category/sub/(?P<pk>\d+)/$', ProductSubCategory_list, name='ProductSubCategory-detail'),
    re_path(r'^product/category/sub/filter/$', ProductSubCategory_filter, name='ProductSubCategory-filter'),
    re_path(r'^product/category/sub/delete/(?P<pk>\d+)/$', ProductSubCategory_delete, name='ProductSubCategory-delete'),

    re_path(r'^product/brand/$', ProductBrand_list, name='ProductBrand-list'),
    re_path(r'^product/brand/(?P<pk>\d+)/$', ProductBrand_list, name='ProductBrand-detail'),
    re_path(r'^product/brand/filter/$', ProductBrand_filter, name='ProductBrand-filter'),
    re_path(r'^product/brand/delete/(?P<pk>\d+)/$', ProductBrand_delete, name='ProductBrand-delete'),

    re_path(r'^product/item/$', ProductItem_list, name='ProductItem-list'),
    re_path(r'^product/item/(?P<pk>\d+)/$', ProductItem_list, name='ProductItem-detail'),
    re_path(r'^product/item/filter/$', ProductItem_filter, name='ProductItem-filter'),
    re_path(r'^product/item/delete/(?P<pk>\d+)/$', ProductItem_delete, name='ProductItem-delete'),
    
    re_path(r'^product/savefile/', SaveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)