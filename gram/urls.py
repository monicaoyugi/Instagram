from django.conf.urls.static import static
from django.conf import settings
from django . import views
from django.urls import path

urlpatterns[

    path('', views.index, name = 'indexPage'),
    path('search', views.search_results, name='search_results'),
    

]