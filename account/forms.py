from django import forms

from .models import Account


class AccountPostForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = {'id_account', 'name_account','password', 'id_per' }
		
		