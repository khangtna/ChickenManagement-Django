from django import forms

from .models import EMPs


class CreateEMPPostForm(forms.ModelForm):

	class Meta:
		model = EMPs
		fields = { 'id','l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','id_account' }
		
		