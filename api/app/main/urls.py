from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    re_path(r'^purchase/order/$', PurchaseOrder_list, name='PurchaseOrder-list'),
    re_path(r'^product/order/(?P<pk>\d+)/$', PurchaseOrder_list, name='PurchaseOrder-detail'),
    re_path(r'^product/order/filter/$', PurchaseOrder_filter, name='PurchaseOrder-filter'),
    re_path(r'^product/order/delete/(?P<pk>\d+)/$', PurchaseOrder_delete, name='PurchaseOrder-delete'),
    
    re_path(r'^purchase/items/$', PurchaseItems_list, name='PurchaseItems-list'),
    re_path(r'^product/items/(?P<pk>\d+)/$', PurchaseItems_list, name='PurchaseItems-detail'),
    re_path(r'^product/items/filter/$', PurchaseItems_filter, name='PurchaseItems-filter'),
    re_path(r'^product/items/delete/(?P<pk>\d+)/$', PurchaseItems_delete, name='PurchaseItems-delete'),

    re_path(r'^purchase/transact/$', PurchaseTransaction_list, name='PurchaseTransaction-list'),
    re_path(r'^product/transact/(?P<pk>\d+)/$', PurchaseTransaction_list, name='PurchaseTransaction-detail'),
    re_path(r'^product/transact/filter/$', PurchaseTransaction_filter, name='PurchaseTransaction-filter'),
    re_path(r'^product/transact/delete/(?P<pk>\d+)/$', PurchaseTransaction_delete, name='PurchaseTransaction-delete'),

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