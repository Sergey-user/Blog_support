from django.urls import path

from .views import *

urlpatterns = [
	path('', blog_page, name='blog_page_url'),
	path('post/create', PostCreate.as_view(), name='post_create_url'),
	path('post/<str:slug>/', post_detail, name='post_detail_url'),
	path('tags/', tags_list, name='tags_list_url'),
	path('tag/create', TagCreate.as_view(), name='tag_create_url'),
	path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
	path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url')

]
