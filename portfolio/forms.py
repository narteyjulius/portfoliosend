from django import forms
from .models import ContactMessage
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-md p-3', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded-md p-3', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'border rounded-md p-3', 'rows':5, 'placeholder': 'Your message'}),
        }


    
    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msgut
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        # subject = cl_data.get('phone_number')

        msg = f'{name} with email {from_email}'
        # msg += f'\nPhone Number: {subject}\n\n'
        msg += cl_data.get('message')

        # return subject, msg
        return  msg

    def send(self):

        # subject, msg = self.get_info()
        msg = self.get_info()

        send_mail(
            # subject=subject,
            message=msg, 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[settings.EMAIL_HOST_USER]
        )