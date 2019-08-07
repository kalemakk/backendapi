# from django.shortcuts import render
# from rest_framework import viewsets
#
# # Create your views here.
# from .serializers import HeroSerializer, HeSerializer, IssueSerializer, UserSerializer, ProjectSerializer
# from .models import Hero, He, Issue, User, Project
#
#
# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('id')
#     serializer_class = HeroSerializer
#
#
# class HeViewSet(viewsets.ModelViewSet):
#     queryset = He.objects.all().order_by('id')
#     serializer_class = HeSerializer
#
#
# class IssueViewSet(viewsets.ModelViewSet):
#     queryset = Issue.objects.all().order_by('id')
#     serializer_class = IssueSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#
#
# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all().order_by('id')
#     serializer_class = ProjectSerializer