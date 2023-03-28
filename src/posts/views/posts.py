from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
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
        account = get_user_model()
        user = account.objects.get(pk=self.request.user.pk)
        followed_users = user.following.all()
        posts = Post.objects.filter(author__in=followed_users)
        return posts.order_by('-created_at')


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


class LikePostView(View):
    def post(self, request, *args, **kwargs):
        account = get_user_model()
        user_id = self.request.user.pk
        user = account.objects.get(pk=user_id)
        post = Post.objects.get(pk=kwargs.get('pk'))

        # Like post
        post.liked_users.add(user)
        user.liked_posts.add(post)

        # Redirect to the same page
        return redirect('post_detail', pk=kwargs.get('pk'))


class UnlikePostView(View):
    def post(self, request, *args, **kwargs):
        account = get_user_model()
        user_id = self.request.user.pk
        user = account.objects.get(pk=user_id)
        post = Post.objects.get(pk=kwargs.get('pk'))

        # Like post
        post.liked_users.remove(user)
        user.liked_posts.remove(post)

        # Redirect to the same page
        return redirect('post_detail', pk=kwargs.get('pk'))
