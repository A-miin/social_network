from django.urls import path
from post.views import CreatePostView, LikeUnlikePostView

urlpatterns = [
    path('', CreatePostView.as_view(), name='create'),
    path('<int:pk>/like/', LikeUnlikePostView.as_view(), name='like-unlike'),
]
