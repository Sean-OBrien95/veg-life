from django.test import TestCase
from .forms import PostForm, ProfileForm

"""
Test run on forms for creating posts using valid and invalid data
"""
class PostFormTest(TestCase):
    def test_valid_post_form(self):
        form_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'excerpt': 'Test excerpt',
            'featured_image': 'test_image.jpg',
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_post_form(self):
        # Testing with invalid data, in this case, an empty form
        form_data = {}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


"""
Test run on forms for profiles using valid and invalid data
"""
class ProfileFormTest(TestCase):
    def test_valid_profile_form(self):
        form_data = {
            'bio': 'Test bio content.',
            'profile_picture': 'test_image.jpg',
            'favorite_animal': 'Dolphin',
            'vegan_duration': '1-2 years',
            'interests': 'Coding, Reading',
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_profile_form(self):
        # Testing with invalid data, in this case, missing required fields
        form_data = {
            'interests': 'Coding, Reading',
            'favorite_animal': 'Dolphin',
            'vegan_duration': '10 years',
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
