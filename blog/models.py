from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    topic = models.ForeignKey('Topic', null=True, on_delete= models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name