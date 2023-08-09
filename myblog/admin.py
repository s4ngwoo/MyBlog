from django.contrib import admin
from .models import Post, Category, Series, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'create_date', 'category', 'series')
    list_filter = ('language',)
    search_fields = ['title', 'content']
    fields = ['title', 'content', 'author', 'category', 'series', 'tag', 'language']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'published_date')
    search_fields = ['title', 'content']
    fields = ['title', 'content']

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'published_date')
    search_fields = ['title', 'content']
    fields = ['title', 'content']

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'published_date')
    search_fields = ['title', 'content']
    fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Tag, TagAdmin)