from django.urls import path
from post.views import PostListView, PostDetailView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
