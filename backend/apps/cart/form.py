from django import forms
from .models import Order

class CartAddForm(forms.Form):
	quantity = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={"class":"form-control"}
			)
	)
	update = forms.BooleanField(
		widget=forms.HiddenInput()
	)
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'description', 'phone']
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
        }

