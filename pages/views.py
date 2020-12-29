from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid:
            contact = form.save()
            messages.success(request, 'Thank you for the message, a member of staff will get back to you')
            form.clean()
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Failed to send your message. Please ensure the form is valid.')
    else:
        form = ContactForm()
    template = 'pages/contact_us.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

def about_page(request):
    return render(request, 'pages/about_us.html')

def join_page(request):
    return render(request, template, context)
