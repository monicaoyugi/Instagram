from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('image/', views.image_upload,name='upload'),
    path('profile',views.profile_info,name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('search', views.search_user, name='search_results'),
    path('edit/', views.profile_edit, name='edit'),
    path('new_comment/', views.add_comment,name='newComment'),
    path('image_upload/', views.image_upload,name='imageUpload'),
]