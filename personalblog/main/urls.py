from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    # post views
    # url('', views.post_list, name='post_list'),
    url('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    # url('', views.PostListView.as_view(), name='post_list'),
    url('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,
    name='post_detail'),
]