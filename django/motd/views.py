from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from motd.models import Post

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'motd\post_all.html'
    context_object_name = 'posts'
    paginate_by = 30

class PostDV(DetailView):
    model = Post

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'