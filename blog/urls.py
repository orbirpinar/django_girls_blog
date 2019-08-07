from django.urls import path

from . import views

urlpatterns = [
	path('',views.post_list,name='post_list'),
	path('post/<int:pk>',views.post_detail,name='post-detail'),
	path('post/new',views.create_post,name='post-new'),
	path('post/<int:pk>/edit',views.edit_post,name='post-edit'),
	path('register/',views.register,name='register'),
]