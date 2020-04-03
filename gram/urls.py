from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register-authentication"),
    # path('image/', views.image_upload,name='upload'),
    path('accounts/profile/',views.profile_info,name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('search', views.search_results, name='search_results'),
    # path('edit/', views.profile_edit, name='edit'),
    path('new_comment/', views.CommentCreateView.as_view(),name='new_comment'),
    # path('like_images/',views.like_images, name='like_images'),
    # path('image_upload/', views.image_upload,name='imageUpload'),
]