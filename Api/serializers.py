from rest_framework import serializers

from .models import Issue, User, Project, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
         model = Issue
         fields = '__all__'


#
# class DemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = demo
#         fields = ('name', 'city', 'age')

