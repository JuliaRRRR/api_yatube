"""Set of serializers for the API."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post Model."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        """Have no idea what to describe here."""

        fields = ('id', 'text', 'pub_date', 'image', 'group', 'author')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment Model."""

    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        """Have no idea what to describe here."""

        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group Model."""

    class Meta:
        """Have no idea what to describe here."""

        fields = ('id', 'title', 'slug', 'description')
        model = Group
