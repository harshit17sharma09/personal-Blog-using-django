from django.conf.urls import url
from . import views 
from .feeds import LatestPostsFeed


app_name = 'main'
urlpatterns = [
    # post views
    url('', views.post_list, name='post_list'),
    # url('', views.PostListView.as_view(), name='post_list'),
    url('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    url('<int:post_id>/share/',
         views.post_share, name='post_share'),
    url('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    url('feed/', LatestPostsFeed(), name='post_feed'),
    url('search/', views.post_search, name='post_search'),
]