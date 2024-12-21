from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'  


urlpatterns = [
    path('post/', views.PostList.as_view(), name='post-list'),  
    path('post/<int:id>/', views.PostDetail.as_view(), name='post-detail'),


]

