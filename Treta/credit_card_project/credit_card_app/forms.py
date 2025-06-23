# credit_card_app/forms.py
from django import forms
from .models import UserCreditCard

class UserCreditCardForm(forms.ModelForm):
    class Meta:
        model = UserCreditCard
        fields = ['username', 'email','encrypted_credit_card']
    
    email = forms.EmailField(required=True)

    
    def clean(self):
        cleaned_data = super().clean()
        # Custom validation logic, raise ValidationError if invalid
        if cleaned_data.get('username') == 'admin':
            raise forms.ValidationError('Username cannot be "admin"')
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Custom validation logic, raise ValidationError if invalid
        if not email.endswith('.com'):
            raise forms.ValidationError('Invalid email format')
        return email

