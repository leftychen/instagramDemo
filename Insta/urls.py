from django.urls import path
from Insta.views import PostsView, PostDetailView,PostCreateView,PostUpdateView,delete_post

urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    #path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post')
    path('posts/delete/<int:id>',delete_post, name='delete_post')

]