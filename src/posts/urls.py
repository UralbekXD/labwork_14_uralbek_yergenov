from django.urls import path

from .views import PostsListView
from .views import PostsAddView
from .views import PostDetailView

from .views import LikePostView, UnlikePostView
from .views import CommentPostView


from .views import SearchUserView


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('search/', SearchUserView.as_view(), name='search_users'),
    path('create/', PostsAddView.as_view(), name='post_add'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),

    # Like and Unlike post
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),

    # Comment
    path('<int:post_id>/comment/', CommentPostView.as_view(), name='comment_post'),
]
