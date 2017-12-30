from django.contrib import admin

# Register your models here.

from .models import Account, AccountDeletion, EmailAddress

admin.site.register(Account)
admin.site.register(AccountDeletion)
admin.site.register(EmailAddress)
