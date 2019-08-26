from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('CUSTOMER', 'Customer'),
        ('EMPLOYEE', 'Employee'),
    )
    name = models.CharField(max_length=25)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='ADMIN')
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    company_name = models.CharField(max_length=15, null=True, blank=True)


class Issue(models.Model):
    ISSUE_STATUS_CHOICES = (
        ('NEW', 'new'),
        ('PENDING', 'pending'),
        ('RESOLVED', 'resolved'),
    )
    PRIORITY_CHOICES = (
        ('HIGH', 'high'),
        ('LOW', 'low'),
        ('MODERATE', 'moderate'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    issue_name = models.CharField(max_length=50, default="issue")
    issue_assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user', null=True, blank=True )
    issue_submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_submit')

    issue_description = models.CharField(max_length=40, null=True, blank=True)
    attachments = models.FileField(upload_to='uploads/', null=True, blank=True)
    status = models.CharField(default='NEW', choices=ISSUE_STATUS_CHOICES, max_length=10)
    date = models.DateTimeField(auto_now=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=8, default='MODERATE')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CommentBody = models.CharField(max_length=40, null=True, blank=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="issue_comment")
