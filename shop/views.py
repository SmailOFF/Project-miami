from django.shortcuts import render, redirect

# from .forms import RateForm
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q


# Create your views here.
# @login_required(login_url='/users/sign_in')
# def homepage(request):
#     content = Product.objects.all
#     return render(request, 'homepage.html', {'content': content})

def products_list(request):
    product_id = request.GET.get('product')
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    products = Product.objects.all()
    slides = Slide.objects.all()
    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('shop:homepage')
        for item in cart_item:
            item.quantity += 1
            item.save()
    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products
    return render(request, 'homepage.html', {'products': products, 'slides': slides})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'sale.html', {'product': product})


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html',
                  {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price}
                  )


def delete_cart_item(request, pk):
    card_item = CartItem.objects.get(pk=pk).delete()
    return redirect('shop:cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('shop:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('shop:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:cart')


def create_order(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    amount = sum([item.quantity for item in cart_items])
    form = forms.OrderForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price,
            customer=request.user
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price(),
            )

        cart_items.delete()
        return redirect('shop:cart')

    form = forms.OrderForm()
    return render(request, 'order_creation_page.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form})


# def rate_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     reviews = Review.objects.filter(product=product)
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.user = request.user
#             rating.product = product
#             rating.save()
#             return redirect('shop:rate_product', pk=pk)
#     form = RateForm()
#     return render(request, 'homepage.html', {'form': form, 'product': product, 'reviews': reviews})


def orders(request):
    orders_list = Order.objects.all
    return render(request, 'orders.html', {'orders': orders_list})


def sale(request):
    product = Product.objects.all
    return render(request, 'sale.html', {'product': product})


def contact(request):
    contact = Product.objects.all
    return render(request, 'contact.html', {'contact': contact})


def pizza(request, pk):
    category_id = Category.objects.get(pk=pk)
    products = Product.objects.get(category=category_id)
    return render(request, 'pizza.html', {'products': products})


def supy(request):
    product_supy = Product.objects.all
    return render(request, 'supy.html', {'product_supy': product_supy})


def pasta(request, pk):
    category_id = Category.objects.get(pk=pk)
    products = Product.objects.get(category=category_id)
    return render(request, 'pasta.html', {'products': products})


def salaty(request):
    product_salaty = Product.objects.all
    return render(request, 'salaty.html', {'product_salaty': product_salaty})


def drink(request):
    product_drink = Product.objects.all
    return render(request, 'drink.html', {'product_drink': product_drink})


def sladkoe(request):
    product_sladkoe = Product.objects.all
    return render(request, 'sladkoe.html', {'product_sladkoe': product_sladkoe})


def bakaleya(request):
    product_bakaleya = Product.objects.all
    return render(request, 'bakaleya.html', {'product_bakaleya': product_bakaleya})


def antipasta(request):
    product_antipasta = Product.objects.all
    return render(request, 'antipasta.html', {'product_antipasta': product_antipasta})


def combo(request):
    product_combo = Product.objects.all
    return render(request, 'combo.html', {'product_combo': product_combo})
