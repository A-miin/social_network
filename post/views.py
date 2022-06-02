from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from post.models import Post
from post.serializers import PostSerializer


class CreatePostView(CreateAPIView):
    model = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


def method_permission_classes(classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


class LikeUnlikePostView(APIView):

    @method_permission_classes([permissions.IsAuthenticated, ])
    def post(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response({'pk': _('Post does not exists')}, status=404)
        post.like.add(self.request.user)
        return Response({'id': post.id}, status=200)

    @method_permission_classes([permissions.IsAuthenticated, ])
    def delete(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response({'pk': _('Post does not exists')}, status=404)
        post.like.remove(self.request.user)
        post.save()
        return Response({'id': post.id}, status=204)
