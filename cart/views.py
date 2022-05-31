from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     count_product=cd['count_product'],
                     update_count_product=cd['update_count_product'])
    else:
        cart.add(product=product)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_count_form']=CartAddProductForm(initial={
            'count_product':item['count_product'],
            'update_count_product':True})
    return render(request, 'cart/detail.html', {'cart': cart})