from django.contrib import admin
from .models import User , Post ,Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'created_at', 'updated_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ('user','post_text', 'created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post', 'comments_text','replys','created_at', 'updated_at')


admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

