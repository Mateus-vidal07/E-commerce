from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartProductForm

# Create your views here.
#listagem de produtos
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(avaliable=True)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
	return render (request, 'shop/product/list.html', {'categories': categories, 'products': products})

def female_product_list(request):
	femininos = Product.objects.filter(slug="feminino")
	context = {'femininos' : femininos }
	return render(request, 'shop/product/femininos.html', context)

def male_product_list(request):
	male = Product.objects.filter(slug="masculino")

	return render(request, 'shop/product/masculino.html', {'male':male})

def acessorios_list(request):
	acessorios = Product.objects.filter(slug="acessorios-sapatos")
	return render(request, 'shop/product/acessorios.html', {'acessorios':acessorios})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, avaliable=True)
	cart_product_form = CartProductForm()
	return render(request, 'shop/product/detail.html', {'cart_product_form':cart_product_form, 'product':product})