from django.test import TestCase

from .models import Post


def test_get_absolute_url(self):
    post = Post.objects.get(id=1)
    # This will also fail if the urlconf is not defined.
    self.assertEquals(post.get_absolute_url(), '/blog/post/1')

# Create your tests here.
