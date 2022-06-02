from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'like')

    def get_current_user(self):
        request = self.context.get('request', None)
        if request:
            return request.user

    def create(self, validated_data):
        post = Post(**validated_data)
        post.author = self.get_current_user()
        post.save()
        return post
