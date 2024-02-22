from django.contrib import admin

from .models import Aircraft, Flight

admin.site.register(Aircraft)
admin.site.register(Flight)
