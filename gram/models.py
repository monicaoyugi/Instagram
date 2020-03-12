from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = HTMLField()
    username=models.CharField(max_length=20,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.profile_photo.url

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
       

    @classmethod
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio
        
    @classmethod
    def get_user(cls,name):
        usernames=cls.objects.filter(username__icontains=name)
        return usernames   


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,new_caption):
        cls.objects.filter(pk = id ).update(image_caption = new_caption)
        new_caption_object = cls.objects.get(image_caption=new_caption)
        new_caption = new_caption_object.image_caption
        return new_caption

    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image

    def __str__(self):
        return self.image_name

class Comments(models.Model):
    comment = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment
