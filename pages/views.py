from django.shortcuts import render

def contact_page(request):
    return render(request, 'pages/contact-us.html')

def about_page(request):
    return render(request, 'pages/about-us.html')
