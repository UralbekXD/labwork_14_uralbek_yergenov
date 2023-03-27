from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
