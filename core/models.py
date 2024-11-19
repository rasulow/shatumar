from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.core.files.base import ContentFile
import io


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Category'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    img = models.ImageField(blank=True, null=True, upload_to='category_images/')
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def img_size(self):
        if self.img and hasattr(self.img, 'size'):
            return f"{self.img.size / 1024:.2f} KB"
        return 0
    
    def save(self, *args, **kwargs):
        if self.img:
            img = Image.open(self.img)
            

            max_width = 1024
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)  # Updated resampling method

            img_io = io.BytesIO()
            img.save(img_io, format='png', quality=85)
            img_content = ContentFile(img_io.getvalue(), self.img.name)

            self.img.save(self.img.name, img_content, save=False)

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
        
        

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.name} - Image {self.id}"
    
    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ['-created_at']
        
        
        
class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else f"Banner {self.id}"
    
    
    def img_size(self):
        if self.img and hasattr(self.img, 'size'):
            return f"{self.img.size / 1024:.2f} KB"
        return 0
    
    def save(self, *args, **kwargs):
        if self.img:
            img = Image.open(self.img)

            max_width = 1024
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)  # Updated resampling method

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)
            img_content = ContentFile(img_io.getvalue(), self.img.name)

            self.img.save(self.img.name, img_content, save=False)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['-created_at']
        
        
class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='gallery/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title if self.title else f"Gallery {self.id}"
    
    def img_size(self):
        if self.img and hasattr(self.img, 'size'):
            return f"{self.img.size / 1024:.2f} KB"
        return 0
    
    def save(self, *args, **kwargs):
        if self.img:
            img = Image.open(self.img)

            max_width = 1024
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)  # Updated resampling method

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)
            img_content = ContentFile(img_io.getvalue(), self.img.name)

            self.img.save(self.img.name, img_content, save=False)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ['-created_at']
        
        
        
class Certificates(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='certificates/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title if self.title else f"Certificate {self.id}"
    
    def img_size(self):
        if self.img and hasattr(self.img, 'size'):
            return f"{self.img.size / 1024:.2f} KB"
        return 0
    
    def save(self, *args, **kwargs):
        if self.img:
            img = Image.open(self.img)

            max_width = 1024
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)  # Updated resampling method

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)
            img_content = ContentFile(img_io.getvalue(), self.img.name)

            self.img.save(self.img.name, img_content, save=False)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        ordering = ['-created_at']