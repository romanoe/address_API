from django.contrib import admin

# Register your models here.
from .models import Address



#Register to admin site
admin.site.register(Address)
