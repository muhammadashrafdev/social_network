from django.db import models

# Create your models here.
class User(models.Model):

    TYPE_CHOICES = (
        ('Type1', 'type1'),
        ('Type2', 'type2'),
        ('Type3', 'type3'),
        ('Type4', 'type4'),
    )
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    email       = models.EmailField(unique=True)
    user_name    = models.CharField(max_length=50,unique=True)
    password    = models.CharField(max_length=50)
    type        = models.CharField(max_length=10, choices=TYPE_CHOICES,default='Client')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey('social_app.User', models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'


    def __str__(self):
        return self.first_name


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_text = models.TextField()
    reply = models.ForeignKey('social_app.Comment', models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def replys(self):
        return self.reply.comments_text


    class Meta:

        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

