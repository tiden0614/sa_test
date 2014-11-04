from django.shortcuts import render
import urllib2

# Create your views here.
def index(request):
    context = { 'v_title': 'Top Stories On HackerNews' }
    return render(request, 'sa/index.html', context)
