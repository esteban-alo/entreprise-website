from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    readonly_fields = ('created_date', 'update_date')


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('created_date', 'update_date')
    list_display = ('title', 'author', 'published', 'post_categories')  # Add more columns to Post Admin
    ordering = ('author', 'published')
    search_fields = ('title', 'author', 'author__username', 'categories__name',)  # Add a search field
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name',)  # Add a list filter right column

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = 'Categories'  # Rename 'post_categories' column to 'Categories'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

