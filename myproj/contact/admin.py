from django.contrib import admin
from contact.models import ContactForm


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(ContactForm, ContactAdmin)
