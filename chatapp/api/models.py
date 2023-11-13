from django.utils import timezone
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,null=True)
    birthDate=models.DateField(default=timezone.now)
    age=models.IntegerField(default=18)
    phone_number= models.CharField(max_length=10,null=True)
    verification_status=models.CharField(max_length=20,default='pending')
    verification_slug=models.CharField(max_length=100,null=True)
    otp =models.CharField(max_length=6, null=True)
    otp_validity =models.BooleanField(default=False)
    resetToken=models.CharField(max_length=50,default="none")
    prfImg = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.username


class Group(models.Model):
    grpid = models.AutoField(primary_key=True)
    grpName = models.CharField(max_length=255)
    grpDescription = models.TextField()
    grpIcon = models.ImageField(upload_to='group_icons/', null=True, blank=True)
    usersList = models.JSONField()

    # def __str__(self):
    #     return self.grpName

class PersonalMsgs(models.Model):
    msgId = models.AutoField(primary_key=True)
    senderId = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()  # This can be extended to support text, image, or video
    sendTime = models.DateTimeField(auto_now_add=True)
    VIEW_STATUS_CHOICES = [
        ('received', 'Received'),
        ('read', 'Read'),
        ('not_received', 'Not Received'),
    ]
    viewStatus = models.CharField(max_length=20, choices=VIEW_STATUS_CHOICES, default='not_received')

    # def __str__(self):
    #     return f'Message {self.msgId} from {self.senderId.username}'

class Story(models.Model):
    storyId = models.AutoField(primary_key=True)
    setBy = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(upload_to='story_content/')
    setTime = models.DateTimeField(auto_now_add=True)
    viewedBy = models.JSONField(default=dict)

    # def __str__(self):
    #     return f'Story {self.storyId} set by {self.setBy.username}'

class GrpMsg(models.Model):
    msgId = models.AutoField(primary_key=True)
    senderId = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()  # This can be extended to support text, image, or video
    sendTime = models.DateTimeField(auto_now_add=True)
    VIEW_STATUS_CHOICES = [
        ('received', 'Received'),
        ('read', 'Read'),
        ('not_received', 'Not Received'),
    ]
    viewStatus = models.CharField(max_length=20, choices=VIEW_STATUS_CHOICES, default='not_received')

    # def __str__(self):
    #     return f'Group Message {self.msgId} from {self.senderId.username}'