from django import forms

from .models import Products


class CreateProductPostForm(forms.ModelForm):

	class Meta:
		model = Products
		fields = {'id_product','name', 'id_category','price', 'status' }
		
		