from django.forms import ModelForm
from .models import Category, Product

class NewCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class NewItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']