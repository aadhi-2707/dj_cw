from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def welcome(request):
    username = request.GET.get('username', 'Guest')
    form_data = request.GET.items()
    return render(request, 'welcome.html', {'username': username, 'form_data': form_data})