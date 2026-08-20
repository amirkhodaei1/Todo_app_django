from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ...models import Todo
from .paginations import DefaultPagination
from .permissions import isOwnerOrReadOnly
from .serializers import TodoSerializer


class TodoModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = TodoSerializer
    queryset = Todo.objects.filter(status=True)

    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({"detail": "ok"})

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "user": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
