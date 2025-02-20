from django.views.generic import TemplateView
from django.db.models import Count, OuterRef, Subquery
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        galleries = cache.get_or_set('galleries',
                                     lambda: models.Gallery.objects.filter(is_active=True),
                                     timeout=300)
        context['galleries'] = galleries

        categories = cache.get_or_set('categories',
                                      lambda: models.Category.objects.annotate(product_count=Count('product')),
                                      timeout=300)
        context['categories'] = [categories[i:i + 8] for i in range(0, len(categories), 8)]

        banners = cache.get_or_set('banners',
                                   lambda: models.Banner.objects.filter(is_active=True),
                                   timeout=300)
        context['banners'] = banners

        products = cache.get_or_set('products',
                                    lambda: models.Product.objects.all().annotate(
                                        img=Subquery(
                                            models.ProductImage.objects.filter(product=OuterRef('id'))
                                            .values('img')[:1]
                                        )
                                    ),
                                    timeout=300)
        context['products'] = products
        context['products_count'] = products.count()

        certificates = cache.get_or_set('certificates', lambda: models.Certificates.objects.filter(is_active=True), 300)
        context['certificates'] = certificates

        return context


class ProductsView(TemplateView):
    template_name = 'pages/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = cache.get_or_set('categories',
                                      lambda: models.Category.objects.all().annotate(product_count=Count('product')),
                                      300)
        brands = cache.get_or_set('brands', lambda: models.Brand.objects.all(), 300)
        sizes = cache.get_or_set('sizes', lambda: models.ProductSize.objects.all(), 300)

        products = cache.get_or_set('products',
                                    lambda: models.Product.objects.all().select_related('category').annotate(
                                        img=Subquery(
                                            models.ProductImage.objects.filter(
                                                product=OuterRef('id')
                                            ).values('img')[:1]
                                        )
                                    ), 300)

        category_slug = self.request.GET.get('category', None)
        brand_slug = self.request.GET.get('brand', None)
        size = self.request.GET.get('size', None)
        if category_slug:
            products = products.filter(category__slug=category_slug)

        if brand_slug:
            products = products.filter(brand__slug=brand_slug)

        if size:
            products = products.filter(size__size=size)

        search = self.request.GET.get('search', None)
        if search:
            products = products.filter(name__icontains=search)
        paginator = Paginator(products, 9)
        page_number = self.request.GET.get('page')

        try:
            products_page = paginator.get_page(page_number)
        except (PageNotAnInteger, EmptyPage):
            products_page = paginator.page(1 if not page_number else paginator.num_pages)

        context['categories'] = categories
        context['brands'] = brands
        context['sizes'] = sizes
        context['products'] = products_page

        galleries = cache.get_or_set('galleries', lambda: models.Gallery.objects.filter(is_active=True), 300)
        context['galleries'] = galleries

        return context


class ProductDetailView(TemplateView):
    template_name = 'pages/product-detail.html'

    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)

        product = cache.get_or_set(f'product_{slug}', lambda: models.Product.objects.get(slug=slug))
        context['product'] = product

        images = cache.get_or_set(f'images_{slug}', lambda: models.ProductImage.objects.filter(product=product))
        context['images'] = images

        galleries = cache.get_or_set('galleries', lambda: models.Gallery.objects.filter(is_active=True), 300)
        context['galleries'] = galleries

        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = cache.get_or_set('certificates', lambda: models.Certificates.objects.filter(is_active=True), 300)
        context['certificates'] = certificates

        galleries = cache.get_or_set('galleries', lambda: models.Gallery.objects.filter(is_active=True), 300)
        context['galleries'] = galleries

        return context
