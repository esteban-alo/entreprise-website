from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request: HttpResponse):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Send mail
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "La Caffettiera: New message",  # About
                "From {} <{}>\n\nWrote: \n\n{}".format(name, email, content),  # Message
                "no-reply@somemail.com",  # From
                ["change_this_mail@mail.com"],  # To
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")

    context = {
        'form': contact_form
    }
    return render(request, "contact/contact.html", context=context)

