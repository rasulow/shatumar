from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('product-detail/', views.ProductsView.as_view(), name='product-detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]