from django.urls import path

from .views import PostsListView
from .views import PostsAddView
from .views import PostDetailView

from .views import SearchUserView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('search/', SearchUserView.as_view(), name='search_users'),
    path('create/', PostsAddView.as_view(), name='post_add'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
]
