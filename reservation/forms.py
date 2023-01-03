from django import forms
from .models import BookingSection
from django.forms import SelectDateWidget
from .widget import DatePickerInput


class BasicInfo(forms.ModelForm):
    class Meta:
        model = BookingSection
        fields = ('subject','user_name','user_email', 'user_mobile')
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'JMÉNO A PŘÍJMENÍ'}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'E-MAIL'}),
            'user_mobile': forms.TextInput(attrs={'placeholder': 'TELEFONNÍ ČÍSLO'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].label = ''
        self.fields['user_name'].label = ''
        self.fields['user_email'].label = ''
        self.fields['user_mobile'].label = ''
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})


class DateForm(forms.ModelForm):
    class Meta:
        model = BookingSection
        fields = ('date',)
        widgets = {
            'date': DatePickerInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].label = ''


class TimeForm(forms.ModelForm):
    class Meta:
        model = BookingSection
        fields = ('time',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].label = ''
        self.fields['time'].widget.attrs.update({'class': 'form-control-time'})