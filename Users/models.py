from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
# from django.contrib import auth

# Create your models here.
""" class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) """

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

class Document(models.Model):
    user = models.ForeignKey(User, related_name='document', on_delete=models.CASCADE)
    title = models.TextField(default="No Title")
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return f'{self.user.username} Document'