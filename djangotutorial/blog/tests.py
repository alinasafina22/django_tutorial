import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Post


def create_post(title, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(title=title, text="text", pub_date=time)


class PostIndexViewTests(TestCase):

    def test_no_posts(self):
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "No posts yet.")

    def test_past_post(self):
        post = create_post("Past", -5)
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, post.title)

    def test_future_post(self):
        create_post("Future", 5)
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "No posts yet.")
