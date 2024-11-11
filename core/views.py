from django.views.generic import TemplateView
from django.db.models import Count, OuterRef, Subquery
from django.core.cache import cache
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        galleries = cache.get('galleries')
        if not galleries:
            galleries = models.Gallery.objects.filter(is_active=True)
            cache.set('galleries', galleries, 300)
        context['galleries'] = galleries

        categories = cache.get('categories')
        if not categories:
            categories = models.Category.objects.all().annotate(product_count=Count('product'))
            cache.set('categories', categories, 300)
        context['categories'] = [categories[i:i+8] for i in range(0, len(categories), 8)]

        banners = cache.get('banners')
        if not banners:
            banners = models.Banner.objects.filter(is_active=True)
            cache.set('banners', banners, 300)
        context['banners'] = banners

        products = cache.get('products')
        if not products:
            products = models.Product.objects.all().annotate(
                img=Subquery(
                    models.ProductImage.objects.filter(
                        product=OuterRef('id')
                    ).values('img')[:1]
                )
            )
            cache.set('products', products, 300)
        context['products'] = products
        context['products_count'] = products.count()

        return context

class ProductsView(TemplateView):
    template_name = 'pages/products.html'


class ProductDetailView(TemplateView):
    template_name = 'pages/product-detail.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'