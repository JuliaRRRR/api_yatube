"""Set of serializers for the API."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post Model."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        """Have no idea what to describe here."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment Model."""

    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Have no idea what to describe here."""

        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group Model."""

    class Meta:
        """Have no idea what to describe here."""

        fields = '__all__'
        model = Group
