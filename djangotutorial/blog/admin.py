from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    list_filter = ("pub_date",)
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "created_at")
