from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('category/<int:category_id>', views.CategoryListView.as_view(), name='category_list_url'),
    path('detail/<slug:slug>', views.PostDetailView.as_view(), name='post_detail_url'),
    path('post/create', views.PostCreateView.as_view(), name='post_create_url'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update_url'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete_url'),
    path('', views.PostsListView.as_view(), name='post_list_url'),

]
