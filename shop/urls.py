from . import views
from .apps import ShopConfig 
from django.urls import path, include

app_name=ShopConfig.name

urlpatterns=[
    path('product/<int:id>',views.product_detail, name='product_detail'),    
    path("<slug:category_slug>/",
    views.product_list,name='product_list_by_category'),
    path('', views.product_list,name="product_list"),
    path('cart/',include('cart.urls', namespace='cart')),
    
    ]