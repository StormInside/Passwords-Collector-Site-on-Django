from django.contrib import admin

from .models import Passwords

# # admin.site.unregister(User)
admin.site.register(Passwords)