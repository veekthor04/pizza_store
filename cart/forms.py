from django import forms
from orders.models import Topping

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField( choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
class CartAddProductForm1(forms.Form):
	quantity = forms.TypedChoiceField( choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
	topping = forms.ModelMultipleChoiceField( widget = forms.CheckboxSelectMultiple, required=False, queryset = Topping.objects.all())
