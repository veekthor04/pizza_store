from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from orders.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartAddProductForm1

# Create your views here.
@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	if (str(product.category) == 'pizza'):
		form = CartAddProductForm1(request.POST)
	else:
		form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		if (str(product.category) != 'pizza'):
			cd['topping'] = None
		cart.add(product=product, topping=cd['topping'], quantity=cd['quantity'], override_quantity=cd['override'])
	return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
	return render(request, 'cart/detail.html', {'cart': cart})
