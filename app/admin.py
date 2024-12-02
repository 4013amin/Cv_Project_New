from .models import Customer, blogs, CategoryWeblog, OtherExample, ImageOtherExample, ImageOtherExampleMobile

from django.contrib import admin


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


@admin.register(OtherExample)
class OtherExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'des']


@admin.register(ImageOtherExample)
class ImageOtherExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'image1']


@admin.register(ImageOtherExampleMobile)
class ImageOtherExampleMobileAdmin(admin.ModelAdmin):
    list_display = ['id', 'image1']


@admin.register(blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']


@admin.register(CategoryWeblog)
class CategoryWeblogAdmin(admin.ModelAdmin):
    list_display = ['name']
