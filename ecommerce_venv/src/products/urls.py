from django.urls import path
from . views import *

urlpatterns=[
    path('',index),
    path('test/',testFunc),
    path('addproduct/',post_product),
    path('addcategory/',post_category),
    path('updateproduct/<int:product_id>',update_product),
    path('deleteproduct/<int:product_id>',delete_product),
   
]