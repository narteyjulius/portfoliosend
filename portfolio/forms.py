from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-md p-3', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded-md p-3', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'border rounded-md p-3', 'rows':5, 'placeholder': 'Your message'}),
        }
