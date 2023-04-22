from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view() ),
    path('users/create/', CreateUser.as_view() ),
    
    path('posts/', PostList.as_view() ),
    path('posts/create/', CreatePost.as_view()),
]