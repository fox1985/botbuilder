
# Register your models here.
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import BotBlock

@admin.register(BotBlock)
class BotBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'next_block')
    search_fields = ('title', 'message')
    list_filter = ('next_block',)
