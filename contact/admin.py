from django.contrib import admin
from .models import Contact, About

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'message')
    list_display_links = ('name', 'email', 'message')



admin.site.register(Contact, ContactAdmin)
admin.site.register(About)