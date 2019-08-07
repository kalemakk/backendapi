"""issueTrackerApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Api.views
import Api.api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('Api.urls')),
    path('api/comment/', Api.api_view.CommentList.as_view()),
    path('api/issue/', Api.api_view.IssueList.as_view()),
    path('api/project/', Api.api_view.ProjectList.as_view()),
    path('api/user/', Api.api_view.UserList.as_view()),
    path('api/project/new', Api.api_view.ProjectCreate.as_view()),
    path('api/user/new', Api.api_view.UserRetriveUpdate.as_view()),

    # path('api/new', Api.api_view.DemoCreate.as_view())
    # path('', include('Users.urls')),
]

