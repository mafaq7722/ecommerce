
from django.urls import path

from . import views

urlpatterns = [


    path('', views.products, name='products'),
    path('details/<int:product_id>', views.product_detail, name='details'),

]

