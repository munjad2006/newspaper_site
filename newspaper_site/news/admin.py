from django.contrib import admin
from .models import Article, ContactForm, ContributeForm

admin.site.register(Article)
admin.site.register(ContactForm)
admin.site.register(ContributeForm)
