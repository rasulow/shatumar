from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin, TabularInline


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')


class ProductImageInline(TabularInline):
    model = models.ProductImage
    extra = 5


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'slug', 'available', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('available', 'category')
    readonly_fields = ('created_at', 'updated_at')
    
    

@admin.register(models.Banner)
class BannerAdmin(ModelAdmin):
    list_display = ('title', 'img', 'description', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    
    

@admin.register(models.Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('title', 'img', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    
    
@admin.register(models.Certificates)
class CertificatesAdmin(ModelAdmin):
    list_display = ('title', 'img', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')