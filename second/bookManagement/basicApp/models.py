import black
from django.utils import timezone
from django.db import models
from django.urls import reverse
import datetime
from accounts.models import User
import uuid
# Create your models here.

class Repositories(models.Model):
    domainChoices = (('Chemistry', 'Chemistry'), ('Robotics', 'Robotics'), ('Phychology', 'Phychology'))
    domain = models.CharField(max_length=50, choices=domainChoices)

    user = models.ForeignKey('auth.User', related_name='repoOwner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)

    progress_title = models.CharField(max_length=100)
    progress_detail = models.TextField(null=True, blank=True)
    progress_video = models.URLField(null=True, blank=True)
    progress_image = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('basicApp:RepoDetailView', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Commit(models.Model):
    commit_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commitTitle = models.CharField(max_length=50)
    textFile = models.URLField(blank=True)
    videoFile = models.URLField(blank=True)
    imageFile = models.ImageField(blank=True)

    def __str__(self):
        return self.commitTitle