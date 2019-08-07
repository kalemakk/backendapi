from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Comment, Issue, User, Project
from .serializers import CommentSerializer, IssueSerializer, UserSerializer, ProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError
git 
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
    search_fields = '__all__'
    # pagination_class = DemoPagination


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = '__all__'
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


class UserRetriveUpdate(RetrieveUpdateAPIView):
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
