from django.shortcuts import render
from contact.models import ContactForm


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')
        
        data = ContactForm(name=name, email=email, message=message)
        data.save()
    return render(request, 'contact.html')
