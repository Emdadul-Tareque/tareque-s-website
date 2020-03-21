from django.contrib import admin

from blog_app.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    list_display = ['title', 'category']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
