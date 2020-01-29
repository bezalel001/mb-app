from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):

  def setUp(self):
    Post.objects.create(title='Software Engineer', text='I am a full-stack Software Engineer')
  

  def test_title_content(self):
    post=Post.objects.get(id=1)
    expected_object_name = f'{post.title}'
    self.assertEqual(expected_object_name, 'Software Engineer')

  def test_text_content(self):
    post=Post.objects.get(id=1)
    expected_object_content = f'{post.text}'
    self.assertEqual(expected_object_content, 'I am a full-stack Software Engineer')



class HomePageViewTest(TestCase):
  def setUp(self):
    Post.objects.create(title='occupation', text='Backend Engineer')

  def test_view_url_exists_at_proper_location(self):
    resp = self.client.get('/')
    self.assertEqual(resp.status_code, 200)

  
  def test_view_url_by_name(self):
    resp = self.client.get(reverse('home'))
    self.assertEqual(resp.status_code, 200)

  
  def test_view_uses_correct_template(self):
    resp = self.client.get(reverse('home'))
    self.assertEqual(resp.status_code, 200)
    self.assertTemplateUsed(resp, 'home.html')
    