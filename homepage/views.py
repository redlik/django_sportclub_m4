from django.shortcuts import render

def index(request):
    """ View to display homepage """
    return render(request, 'homepage/index.html')
