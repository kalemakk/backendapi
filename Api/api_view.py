from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Comment, Issue, User, Project
from .serializers import CommentSerializer, IssueSerializer, UserSerializer, ProjectSerializer, GetUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

#
# class DemoPagination(LimitOffsetPagination):
#     default_limit = 2
#     max_limit = 5


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name',)
    # pagination_class = DemoPagination


class IssueList(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('status', 'priority')
    # pagination_class = DemoPagination


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('role', 'id')
    # pagination_class = DemoPagination


class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('id', 'name')
    # pagination_class = DemoPagination


class ProjectCreate(CreateAPIView):

    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserCreate(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class IssueCreate(CreateAPIView):
    serializer_class = IssueSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CommentCreate(CreateAPIView):
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'

    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        user_id = request.data.get('id')
        response = super().delete(request, *args, *kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('user_data_{}'.format(user_id))
        return response


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        comment_id = request.data.get('id')
        response = super().delete(request, *args, *kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('comment_data_{}'.format(comment_id))
        return response


class IssueRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    lookup_field = 'id'

    serializer_class = IssueSerializer

    def delete(self, request, *args, **kwargs):
        issue_id = request.data.get('id')
        response = super().delete(request, *args, *kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('issue_data_{}'.format(issue_id))
        return response


class ProjectRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    lookup_field = 'id'

    serializer_class = ProjectSerializer

    def delete(self, request, *args, **kwargs):
        project_id = request.data.get('id')
        response = super().delete(request, *args, *kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('project_data_{}'.format(project_id))
        return response














# class DemoCreate(CreateAPIView):
#     serializer_class = DemoSerializer
#
#     def create(self, request, *args, **kwargs):
#         try:
#             name = request.data.get('name')
#             if name is not None:
#                 raise ValidationError({'name': 'Name must be entered'})
#
#         except ValueError:
#             raise ValidationError({'name': 'plse name should be entered'})
#
#         return super().create(self, request, *args, **kwargs)
