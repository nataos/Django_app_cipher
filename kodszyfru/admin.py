from django.contrib import admin
from  . models import Passwords
# Register your models here.
admin.site.register(Passwords)

#@admin.register(Passwords)

#class PasswordsAdmin(admin.ModelAdmin):
    #fields = ['text', 'cipher']
    #exclude = ['text']
    #list_display = ['text']
    #list_filter = ['text']
 #   search_fields = ['text']