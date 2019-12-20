from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView , ListView
from .models import User , Post ,Comment
import json

# Create your views here.
class HomeView(ListView):
    template_name = 'index.html'
    model = User

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post_objects'] = Post.objects.all()
        context['comment_objects'] = Comment.objects.all()
        return context
class PostView():

    def post(self):
        pass

def create_post(request):

    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        print(post_text)

        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        # response_data['postpk'] = post.pk
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )