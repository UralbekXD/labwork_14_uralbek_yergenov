from django.urls import path

from .views import SignUpView, LoginView, logout_view
from .views import ProfileDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
]
