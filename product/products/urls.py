from django.urls import path,include
from . import views
from . import models
from django.conf import settings

urlpatterns=[
    path("",views.all_products,name='all_products'),
    path("add/",views.add_products,name='add_products'),
    path("edit/<int:product_id>",views.edit_product,name='edit_product'),
    path("delete/<int:product_id>",views.delete_product,name='delete_product'),
]