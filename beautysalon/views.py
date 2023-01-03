from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm

def home(request):
    form = ContactForm()
    return render(request, 'beautysalon/home.html', {'form': form})

def email_save_contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('beautysalon/emails/contactform.html', {
                'name':name,
                'email':email,
                'message':message
            })
            send_mail(name, message, email, ['djangotestsalon@gmail.com'], html_message=html)
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'beautysalon/home.html', {'form': form})
