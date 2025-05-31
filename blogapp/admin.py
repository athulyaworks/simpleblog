from django.contrib import admin
from .models import Blog, Author, Category

# Register your models here.

class BlogInline(admin.TabularInline):
    model = Blog
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','category','published_date')
    search_fields = ('title', 'content')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [BlogInline] 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)