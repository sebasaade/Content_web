from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date')

admin.site.register(About, AboutAdmin)