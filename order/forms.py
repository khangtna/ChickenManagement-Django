from django import forms

from .models import OrderDetails


class CreateOrderdetailPostForm(forms.ModelForm):

	class Meta:
		model = OrderDetails
		fields = {'id_orderdetail','id_Order', 'id_Product', 'quantity' }
		
		