from django.contrib import admin
from .models import Pattern, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Comment)

@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):

    list_display = ('pattern_name', 'slug', 'status')
    search_fields = ['pattern_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('pattern_name',)}
    summernote_fields = ('instructions',)