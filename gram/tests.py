from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from  . models import *

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.image_one = Image(image='image/paris.jpg',image_name='monica',image_caption='paris is one of the most beutiful cities',likes=20, id=1,user_id=4)

    def test_instance(self):
        Image.Objects.all().delete()
        self.assertTrue(isinstance(self.image_one,Image))

    def test_save_method(self):
        self.image_one.save_image()
        images = image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) is 0)
    
    def test_update_method(self):
        self.image_one.save()
        new_caption = 'one of the most beutiful cities'
        done = self.image_one.update_caption(self.image_one.id,new_caption)
        self.assertEqual(done,new_caption)

    def tearDown(self):
        Image.objects.all().delete()

