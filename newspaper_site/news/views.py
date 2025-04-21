from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ContactForm, ContributeForm
from django.contrib import messages



def home(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'news/home.html', {'articles': articles})

def about(request):
    return render(request, 'news/about.html')

def news(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'articles': articles})

def explain(request):
    return render(request, 'news/explain.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the ContactForm model
        contact_form = ContactForm(name=name, email=email, message=message)
        contact_form.save()

        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to the same page or another page

    return render(request, 'news/contact.html')

def contribute(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        pub_date = request.POST.get('pub_date')
        explanation = request.POST.get('explanation')

        # Save the data to the ContributeForm model
        contribute_form = ContributeForm(title=title, name=name, pub_date=pub_date, Explanation=explanation)
        contribute_form.save()

        # Add a success message
        messages.success(request, 'Your contribution has been submitted successfully!')
        return redirect('contribute')  # Redirect to the same page or another page

    return render(request, 'news/contribute.html')


def career(request):
    return render(request, 'news/career.html')


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/detail.html', {'article': article})
