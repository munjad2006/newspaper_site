from django.shortcuts import render, get_object_or_404
from .models import Article

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
    return render(request, 'news/contact.html')

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/detail.html', {'article': article})
