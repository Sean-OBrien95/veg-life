from django.contrib import admin
from .models import Post, Comment, UserProfile
from django_summernote.admin import SummernoteModelAdmin

"""
Register the Post model with SummernoteModelAdmin
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


"""
Register the Comment model with a custom admin interface
"""
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register the UserProfile model
admin.site.register(UserProfile)
