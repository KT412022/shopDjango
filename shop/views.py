from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

# Create your views here.
# def about_shop(request):
#    return HttpResponse("Сторінка про магазин")


def about_shop(request):
    return render(request, "shop/about.html")


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 6)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)

    return render(request, 'shop/product/list.html', {
        "category": category,
        "categories": categories,
        "products": page,
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,'cart_product_form': cart_product_form})