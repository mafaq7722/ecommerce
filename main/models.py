from django.db import models


# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class SubCategories(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    sub_categories = models.CharField(max_length=50)

    def __str__(self):
        return str(self.sub_categories)


class Products(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories', null=True)
    subCategories = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='subCategories', null=True)
    product_image = models.ImageField(upload_to='img')
    discount_percentage = models.IntegerField()
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    before_discount_price = models.IntegerField()
    is_trending = models.BooleanField(default=False)
    is_promotions = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class ProductDetail(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products')
    productName = models.CharField(max_length=200)
    display_image = models.ImageField(upload_to='img')
    product_description = models.TextField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.productName


class Product_images(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products_image')
    image = models.ImageField(upload_to='img')


class ProductDescription(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    model_name_description = models.TextField()
    field_1 = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='img')
    description_1 = models.TextField()
    field_2 = models.CharField(max_length=100)
    image2 = models.ImageField(upload_to='img')
    description_2 = models.TextField()
    field_3 = models.CharField(max_length=100)
    image3 = models.ImageField(upload_to='img')
    description_3 = models.TextField()
    field_4 = models.CharField(max_length=100)
    image4 = models.ImageField(upload_to='img')
    description_4 = models.TextField()

    def __str__(self):
        return self.model_name
