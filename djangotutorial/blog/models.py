from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField(auto_now_add=True)

    def is_published(self):
        return self.pub_date <= timezone.now()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]
