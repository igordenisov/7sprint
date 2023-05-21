from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(),
         name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/edit/', 
         login_required(views.PostUpdateView.as_view()),
         name='edit_post'),
    path('posts/<int:pk>/delete/', 
         login_required(views.PostDeleteView.as_view()), name='delete_post'),
    path('category/<slug:category_slug>/', views.CategoryListView.as_view(),
         name='category_posts'),
    path('profile/<slug:username>/',
         views.ProfileListView.as_view(), name='profile'),
    path('edit_profile/', login_required(
     views.ProfileUpdateView.as_view()),
     name='edit_profile'),
    path('posts/<int:pk>/comment/',
         login_required(views.CommentAddView.as_view()), name='add_comment'),
    path('posts/<int:pk>/edit_comment/<int:id>/',
         login_required(views.CommentUpdateView.as_view()),
         name='edit_comment'),
    path('posts/<int:pk>/delete_comment/<int:id>/',
         login_required(views.CommentDeleteView.as_view()),
         name='delete_comment'),
]
