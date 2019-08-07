from django.contrib import admin
from .models import Issue, User, Project, Comment
# Register your models here.

admin.site.register(Issue)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Comment)
