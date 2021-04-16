from math import ceil

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products, Categories, ProductDetail, SubCategories, Product_images, ProductDescription


# Create your views here.


def home(request):
    return render(request, 'base.html')


def products(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    product = Products.objects.all()
    trend = Products.objects.filter(is_trending=True)[:6]
    promotion = Products.objects.filter(is_promotions=True)[:4]
    mobile_product = Products.objects.filter(categories__category='Mobile')[:6]
    tablet_product = Products.objects.filter(categories__category='Tablet')[:6]
    all_products = Products.objects.filter(subCategories__sub_categories='sub_categories_id')
    context = {'categories': categories, 'sub_categories': sub_categories,
               'trend': trend, 'product': product,
               'mobile_product': mobile_product, 'tablet_product': tablet_product,
               'promotion': promotion, 'all_products': all_products}

    return render(request, 'main/index.html', context)


def product_detail(request, product_id):
    details = ProductDetail.objects.get(pk=product_id)
    images = Product_images.objects.filter(products_id=product_id)
    productDescription = ProductDescription.objects.filter(product_id=product_id)
    context = {'details': details, 'images': images, 'productDescription': productDescription}

    return render(request, 'main/product_detail.html', context)

