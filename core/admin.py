from django.contrib import admin
from django.utils import formats
from . import models
from unfold.admin import ModelAdmin, TabularInline, SelectMultiple


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'img_size', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True
    
    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'


class ProductImageInline(TabularInline):
    model = models.ProductImage
    extra = 5


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'slug', 'available', 'category', 'brand', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('name', 'slug', 'brand')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('available', 'category', 'brand')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'
    
    
@admin.register(models.Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'


@admin.register(models.ProductSize)
class ProductSizeAdmin(ModelAdmin):
    list_display = ('size', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('size',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'
    
    
@admin.register(models.Banner)
class BannerAdmin(ModelAdmin):
    list_display = ('title', 'img', 'description', 'is_active', 'img_size', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'


@admin.register(models.Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('title', 'img', 'img_size', 'is_active', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'


@admin.register(models.Certificates)
class CertificatesAdmin(ModelAdmin):
    list_display = ('title', 'img', 'img_size', 'is_active', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    show_full_result_count = True

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'