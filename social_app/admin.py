from django.contrib import admin
from .models import User , Post ,Comment,PostLike,CommentLike
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#
#     list_display = ('first_name', 'created_at', 'updated_at')
#

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','post_text', 'created_at', 'updated_at')

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user','post','flag','created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post', 'comments_text','created_at', 'updated_at')

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('user','comment','flag','created_at', 'updated_at')


# admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(PostLike,PostLikeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(CommentLike,CommentLikeAdmin)


