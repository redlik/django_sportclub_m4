from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


from .models import Contact, Member
from .forms import ContactForm, MemberForm


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
    if request.method == 'POST':
        form = MemberForm(request.POST or None)
        if form.is_valid:
            member = form.save()
            messages.success(request, 'Thanks! We will contact you once your membership is active')
            form.clean()
            print(member.email)
            subject = request.POST.get('email')
            body = render_to_string('pages/membership_email/application.txt', {'member': member})
            admin_email = settings.ADMIN_EMAIL
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [admin_email])
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'We could not process your application. Please ensure the form is valid.')
    else:
        form = MemberForm()
    template = 'pages/join_us.html'

    context = {
        'form': form,
    }
    return render(request, template, context)
