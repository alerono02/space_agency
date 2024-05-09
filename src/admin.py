from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from src.models import SliderImage


class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image', 'title', 'order')
    list_editable = ('order',)


admin.site.register(SliderImage, SliderImageAdmin)
