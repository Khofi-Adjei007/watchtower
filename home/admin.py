from django.contrib import admin

# Register your models here.
from .models import portalUsers
from .models import practice_data

admin.site.register(portalUsers)
admin.site.register(practice_data)