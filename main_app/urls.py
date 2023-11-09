from django.urls import path
from . import views
from .views import PostListView
from .views import YourPostsListView
from .views import PostDelete

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


from .views import custom_403_view



urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='index'),
    path('posts/<int:user_id>/', YourPostsListView.as_view(), name='your_posts'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('post/update/<int:pk>/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/detail/<int:post_id>/', views.posts_detail, name='detail'),
    path('posts/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='comment_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('create/', views.create_image, name='image_create'),
    path('images/', views.image_list, name='image_list'),  # URL for the image list page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)