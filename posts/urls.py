from . import views
from django.urls import path
from .views import user_bookmarks, PostList, view_profile

# Various paths for site navigation
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/<int:user_id>/', view_profile, name='view_profile'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<slug:slug>/like/', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/like/',
         views.like_comment, name='like_comment'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/confirm_delete/',
         views.confirm_delete, name='confirm_delete'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('confirm_profile_delete/', views.confirm_profile_delete,
         name='confirm_profile_delete'),
    path('delete_profile/<int:user_id>/',
         views.delete_profile, name='delete_profile'),
    path('comments/<int:comment_id>/delete/',
         views.delete_comment, name='delete_comment'),
    path('comment_approval/', views.comment_approval, name='comment_approval'),
    path('toggle_bookmark/<int:post_id>/',
         views.toggle_bookmark, name='toggle_bookmark'),
    path('user_bookmarks/', user_bookmarks, name='user_bookmarks'),
    path('posts/', PostList.as_view(), name='post_list'),
]
