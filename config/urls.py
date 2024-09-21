# config/urls.py
from django.contrib import admin
from django.urls import path
from pages.views import home_view, about_view  # Import your home and about views
from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)  # Import post-related views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Home page
    path('about/', about_view, name='about'),  # About page
    path('posts/', PostListView.as_view(), name='list'),  # Post list
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),  # Post detail
    path('posts/new/', PostCreateView.as_view(), name='new'),  # Create new post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),  # Edit post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),  # Delete post
]
