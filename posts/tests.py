from django.test import TestCase
from .models import Posts
from django.utils import timezone
from django.urls import reverse

# Create your tests here.
class PostsModelTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="Sergen",created_date=timezone.now())
    
    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, f"Sergen")


class HomePageTestView(TestCase):
    def setUp(self):
        Posts.objects.create(text="This is another test",created_date=timezone.now())
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('posts:home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/post_list.html')