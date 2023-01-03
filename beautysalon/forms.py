from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Jméno a příjmení'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    message = forms.CharField(max_length=100000,widget=forms.Textarea(attrs={'placeholder': 'Vaše zpráva'}))