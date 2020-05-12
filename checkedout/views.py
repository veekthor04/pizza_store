from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				toppings = ''
				if len(item['topping_list'])>0:
					for value in item['topping_list']:
						toppings+= value + ' '
				OrderItem.objects.create(order=order, product=item['product'], price=item['total_price'], quantity=item['quantity'], topping = toppings)
			# clear the cart
			cart.clear()
			# launch asynchronous task
			order_created(order.id)
			return render(request, 'checkedout/order/created.html', {'order': order})
	else:
		form = OrderCreateForm()
	return render(request, 'checkedout/order/create.html', {'cart': cart, 'form': form})

@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'admin/checkedout/order/detail.html', {'order': order})
