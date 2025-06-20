
# Register your models here.
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import BotBlock, BlockButton


class BlockButtonInline(admin.TabularInline):
    model = BlockButton
    fk_name = 'block'  # 💥 вот это добавь!
    extra = 1


@admin.register(BotBlock)
class BotBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'block_type')
    search_fields = ('title', 'message')
    list_filter = ('block_type',)
    inlines = [BlockButtonInline]


@admin.register(BlockButton)
class BlockButtonAdmin(admin.ModelAdmin):
    list_display = ('block', 'label', 'to_block')
    search_fields = ('label',)
