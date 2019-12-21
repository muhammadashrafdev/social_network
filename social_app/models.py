from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    TYPE_CHOICES = (
        ('1', 'BA'),
        ('2', 'Sup'),
        ('3', 'Man'),
        ('4', 'Exec')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='BA')
    parent = models.ForeignKey('social_app.User', on_delete=models.CASCADE, null=True, blank=True)

# class User(models.Model):
#     TYPE_CHOICES = (
#         ('1', 'BA'),
#         ('2', 'Sup'),
#         ('3', 'Man'),
#         ('4', 'Exec')
#     )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     user_name = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='BA')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     parent = models.ForeignKey('social_app.User',on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         db_table = 'User'
#         verbose_name = 'User'
#
#     def __str__(self):
#         return self.first_name


class Post(models.Model):
    TYPE_CHOICES = (
        ('Initiated', 'Initiated'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Correction', 'Correction'),
        ('Closed', 'Closed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    image = models.ImageField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_actor',default=0)
    last_actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_actor',default=0)
    current_status = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Initiated')

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post_like'
        verbose_name = 'post like'
        verbose_name_plural = 'post like'


class WorkflowLog(models.Model):
    TYPE_CHOICES = (
        ('Initiated', 'Initiated'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Correction', 'Correction'),
        ('Closed', 'Closed')
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Initiated')
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_text = models.TextField()
    reply = models.ForeignKey('social_app.Comment', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def replys(self):
        return self.reply.comments_text

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment_like'
        verbose_name = 'comment like'
        verbose_name_plural = 'comment like'
