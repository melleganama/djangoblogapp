from django.contrib import admin
from article.models import Article, Comment


# Register your models here.

admin.site.register(Article)

#this decorator is a short cut for admin.site.register(Model, ModelAdmin).
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "comment_author", "comment_date")
    list_display_links = ("article", "comment_author")
    list_filter = ("article", "comment_author", "comment_date")
    search_fields = ("title",)
