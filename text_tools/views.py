from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        "data": True
    }
    return render(request, 'index.html', data)