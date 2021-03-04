from django.contrib import admin
from .models import Posts

# Register your models here.
@admin.register(Posts)
class AdminPost(admin.ModelAdmin):
    search_fields = ['text',]
    list_display = ['text', ]
    list_filter = ('created_date', )