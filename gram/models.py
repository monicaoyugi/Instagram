from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.png' ,upload_to='prof_images')
    bio = models.TextField(max_length=120)


class Image(models.Model):
    posted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    caption = models.TextField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    posted_on = models.DateTimeField(default=timezone.now)

class Comments(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment = models.TextField(max_length=150)
    posted_on = models.DateTimeField(default=timezone.now)