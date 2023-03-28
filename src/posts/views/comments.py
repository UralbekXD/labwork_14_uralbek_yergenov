from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from posts.models import Comment


class CommentPostView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'posts/posts_list.html'

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')

        if text:
            account = get_user_model()
            author = account.objects.get(pk=request.user.pk)
            post = Post.objects.get(pk=kwargs.get('post_id'))
            Comment.objects.create(
                author=author,
                post=post,
                text=text,
            )

            post.commented_users.add(author)
            author.commented_posts.add(post)
        return redirect('post_detail', pk=kwargs.get('post_id'))
