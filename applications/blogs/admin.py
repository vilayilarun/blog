from django.contrib import admin

from .models import Blog, Tag, Gallery


class GalleryAdmin(admin.StackedInline):
    model = Gallery

class BlogAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin]
    list_display = ['title', 'date', 'publish']
    list_editable = ['publish']
    filter_horizontal = ['tags']
    readonly_fields = ['visit_count']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)

