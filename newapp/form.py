from django import forms
from newapp.models import *

class AddInvForm(forms.ModelForm):
	class Meta:
		model = Add_Inventory
		fields = ['Product','Unit','Quantity']


class CreateInvForm(forms.ModelForm):
	class Meta:
		model = Create_Inventory
		fields = ['ProductName','Year','Month']


		
		