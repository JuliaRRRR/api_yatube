from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import (ModelViewSet,
                                     ReadOnlyModelViewSet)

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().select_related('author').only(
        'id', 'text', 'pub_date', 'image', 'group', 'author__username')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.get_post().id)
