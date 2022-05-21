from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('cart/create_order', views.create_order, name='create_order'),
    path('rate_product/<int:pk>', views.rate_product, name='rate_product'),
    path('orders/', views.orders, name='orders'),
    path('sale/', views.sale, name='sale'),
    path('contact/', views.contact, name='contact'),
    path('homepage/', views.products_list, name='products'),
    path('supy/', views.supy, name='supy'),
    path('pasta/', views.pasta, name='pasta'),
    path('salaty/', views.salaty, name='salaty'),
    path('drink/', views.drink, name='drink'),
    path('sladkoe/', views.sladkoe, name='sladkoe'),
    path('bakaleya/', views.bakaleya, name='bakaleya'),
    path('antipasta/', views.antipasta, name='antipasta'),
    path('combo/', views.combo, name='combo'),
]
