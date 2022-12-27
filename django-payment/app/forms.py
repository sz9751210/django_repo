from django import forms
from .models import Expense
class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = { # 客製化表單的顯示外觀
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {  # 網頁上顯示的名稱
            'name': '花費項目',
            'price': '金額'
        }