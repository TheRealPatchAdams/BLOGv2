from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),  # List view
    path("new/", views.PostCreateView.as_view(), name="new"),  # Create new post
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),  # Detail view
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),  # Edit post
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),  # Delete post
    #ADD OTHER URLS (NEW PAGES) BELOW
    
]
