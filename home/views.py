from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : 'data send from views'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")
        redirect('/')

    return render(request, 'contact.html')