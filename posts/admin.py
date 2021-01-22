from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title', )}
