# from django.urls import include, path
# from rest_framework import routers
# from . import views
#
# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
# router.register(r'hero', views.HeViewSet)
# router.register(r'issue', views.IssueViewSet)
# router.register(r'user', views.UserViewSet)
# router.register(r'project', views.ProjectViewSet)
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]