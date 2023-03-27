from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from posts.models import Post
from posts.forms import PostAddForm


class SearchUserView(ListView):
    model = get_user_model()
    template_name = 'posts/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.request.GET.get('q')
        account = self.model
        users = account.objects.filter(
            Q(username__icontains=username) |
            Q(email__icontains=username) |
            Q(first_name__icontains=username)
        )

        return users


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        user = self.request.user
        return Post.objects.exclude(author=user).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/posts_detail.html'
    context_object_name = 'post'


class PostsAddView(CreateView):
    model = Post
    form_class = PostAddForm
    template_name = 'posts/posts_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('posts')

        return self.render_to_response(context={
            'form': form,
        })
