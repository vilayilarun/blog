from django.contrib import admin
from .models import Contact


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(Contact, ContactsAdmin)
