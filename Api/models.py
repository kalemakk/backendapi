from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('CUST', 'Customer'),
        ('EMPLOY', 'Employee'),
    )
    name = models.CharField(max_length=25)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=20)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='ADMIN')


class Issue(models.Model):
    ISSUE_STATUS_CHOICES = (
        ('OPEN', 'open'),
        ('PROGRESS', 'progress'),
        ('CLOSED', 'closed'),
    )
    PRIORITY_CHOICES = (
        ('HIGH', 'high'),
        ('LOW', 'low'),
        ('MODERATE', 'moderate'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    issue_name = models.CharField(max_length=50, default="issue")
    issue_submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    # issue_assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.CharField(max_length=40)
    attachments = models.FileField(upload_to='uploads/')
    status = models.CharField(default='OPEN', choices=ISSUE_STATUS_CHOICES, max_length=6)
    date = models.DateTimeField(auto_now=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=8, default='MODERATE')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CommentBody = models.CharField(max_length=40)
