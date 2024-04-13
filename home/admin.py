from django.contrib import admin

# Register your models here.
from .models import portalUsers
from .models import registrations

admin.site.register(portalUsers)
admin.site.register(registrations)