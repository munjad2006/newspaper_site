from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('explain', views.explain, name='explain'),
    path('career', views.career, name='career'),
    path('contribute', views.contribute, name='contribute'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]
