from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    list_filter = [field.name for field in Post._meta.fields if field.name != 'desc']

class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    list_filter = [field.name for field in Comment._meta.fields if field.name != 'desc']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

