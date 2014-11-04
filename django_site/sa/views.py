from django.shortcuts import render
import django.template

# Create your views here.
def index(request):
    context = { 'message': 'test' }
    return render(request, 'sa/index.html', context)
