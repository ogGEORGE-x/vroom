from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message','car']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'car': forms.Select(attrs={'class': 'form-control'}),
        }
class CarForm(forms.Form):
    make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))