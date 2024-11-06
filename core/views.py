from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'pages/products.html')


def product_detail(request):
    return render(request, 'pages/product-detail.html')