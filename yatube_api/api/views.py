"""Configuration Views for API Classes."""
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (ModelViewSet,
                                     ReadOnlyModelViewSet)

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Group, Post


class GroupViewSet(ReadOnlyModelViewSet):
    """API ModelViewSet for accessing Group class."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    """API ModelViewSet for accessing Post class."""

    queryset = Post.objects.all().select_related('author').only(
        'id', 'text', 'pub_date', 'image', 'group', 'author__username')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Save request user object as post author."""
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """API ModelViewSet for accessing Comment class."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self):
        """Get post by id for getting all the comments."""
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        """Get all the comments for a specific post."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Save request user object as comment author."""
        serializer.save(author=self.request.user, post_id=self.get_post().id)
