from __future__ import unicode_literals
from time import time
from django.db import models

# Create your models here.

class Test(models.Model):
    abc = models.CharField(max_length = 12 , null = True)

def productMediaPath(instance , filename):
    return 'ecommerce/static/media/product/%s_%s_%s' % (str(time()).replace('.', '_'), instance.typ,filename)
def categoryMediaPath(instance , filename):
    return 'ecommerce/static/media/category/%s_%s_%s' % (str(time()).replace('.', '_'), instance.typ, filename)
def brandMediaPath(instance , filename):
    return 'ecommerce/static/media/brand/%s_%s_%s' % (str(time()).replace('.', '_'), instance.typ, filename)

MEDIA_TYP = (
    ('thumb' , 'thumb'),
    ('image' , 'image'),
    ('video' , 'video'),
    ('banner' , 'banner')
)

class ProductMedia(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    typ = models.CharField(choices = MEDIA_TYP , default = 'image' , max_length = 15)
    attachment = models.FileField(upload_to = productMediaPath ,  null = True)

class CategoryMedia(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    typ = models.CharField(choices = MEDIA_TYP , default = 'image' , max_length = 15)
    attachment = models.FileField(upload_to = categoryMediaPath ,  null = True)

class BrandMedia(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    typ = models.CharField(choices = MEDIA_TYP , default = 'image' , max_length = 15)
    attachment = models.FileField(upload_to = brandMediaPath ,  null = True)

PRODUCT_META_TYP = (
    ('SSN' , 'SSN'),
    ('HSN' , 'HSN'),
)

class ProductMeta(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    taxCode = models.CharField(max_length = 100 , blank = True)
    taxRate = models.FloatField(null=True, blank=True, default=None)
    typ = models.CharField(choices = PRODUCT_META_TYP , default = 'HSN' , max_length = 15)

class Brand(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    brand_name = models.CharField(max_length = 100 , null = True)
    brand_desc = models.CharField(max_length = 1000 , null = True)
    brand_media = models.ManyToManyField(BrandMedia , related_name='brand_media' , blank = True)

class Category(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    category_name = models.CharField(max_length = 100 , null = True)
    category_desc = models.CharField(max_length = 1000 , null = True)
    category_parent = models.ForeignKey('self' , related_name = 'children' , null= True)
    category_media = models.ManyToManyField(CategoryMedia , related_name='cat_media' , blank = True)

ATTRIBUTE_UNIT_CHOICE = (
    ('cm' , 'cm'),
    ('metre' , 'metre'),
    ('inch' , 'inch'),
    ('gram' , 'gram'),
    ('kilogram' , 'kilogram'),
    ('ton' , 'ton'),
    ('none', 'none')
)

class ProductAtrribute(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    attribute_name = models.CharField(max_length = 100, null = True)
    attribute_value = models.CharField(max_length = 100, null = True)
    attribute_unit =  models.CharField(choices = ATTRIBUTE_UNIT_CHOICE , default = 'none' , max_length = 15)

class Product(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    product_name = models.CharField(max_length = 100, null = False)
    product_sku = models.CharField(max_length = 100, null = False)
    product_price = models.FloatField(null = True, default = None)
    product_weight = models.FloatField(null = True, default = None)
    product_desc = models.CharField(max_length = 1000, null = True)
    product_short_desc = models.CharField(max_length = 500, null = True)
    product_media = models.ManyToManyField(ProductMedia, related_name = 'prod_media' , blank = True)
    product_category = models.ForeignKey(Category, null = False, related_name = 'prod_cat')
    product_brand = models.ForeignKey(Brand, null = True, related_name = 'prod_brand')
    product_meta = models.ForeignKey(ProductMeta, null = True, related_name = 'prod_meta')
    product_attribute = models.ManyToManyField(ProductAtrribute, blank = True, related_name = 'prod_attr')
    product_disc_perc = models.FloatField(null=True, blank=True, default=None)
