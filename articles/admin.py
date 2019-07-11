from django.contrib import admin

# Register your models here.

from .models import Article, Comment

"""
We could display this with either TabularInline or StackedInline.

class CommentInline(admin.TabularInline): # Tabular
    model = Comment
"""

class CommentInline(admin.StackedInline): # Inline
    model = Comment
    """
    By default, the Django admin will display 3 empty rows here. You can change the 
    default number that appear with the extra field.
    """
    extra = 0 # new

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)