from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Account)

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name')
    #list_display_links = ('email', 'first_name')
    #readonly_fields = ('last_login')
    #ordering = ('date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


