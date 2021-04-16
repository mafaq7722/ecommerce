from django.contrib import admin
from .models import Products, Categories, ProductDetail, SubCategories, Product_images, ProductDescription


# Register your models here.


class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ['sub_categories', 'categories']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['subCategories', 'categories', 'product_name', 'product_image', 'price', 'discount_percentage', 'before_discount_price',
                    'is_trending', 'is_promotions']


class Product_imagesAdmin(admin.ModelAdmin):
    list_display = ['products', 'image']


admin.site.register(Products, ProductAdmin)
admin.site.register(Categories)
admin.site.register(ProductDetail)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(Product_images, Product_imagesAdmin)
admin.site.register(ProductDescription)
