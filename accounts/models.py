from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(unique=True,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    modified=models.DateTimeField(auto_now_add=False)
    updated=models.DateTimeField(auto_now=False)
    phone = PhoneNumberField(region='IR', blank=True,null=True, unique=True)
    address=models.CharField(max_length=200,blank=True)
    avatar=models.ImageField(upload_to='avatars/',default='avatars/avatar.jpg')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args, **kwargs):
        super.save(*args, **kwargs)
        if self.avatar and hasattr(self.avatar, 'path'): 
            image = Image.open(self.avatar.path)
            if image.height > 100 or image.width > 100:
                new_image = (100, 100)
                image.thumbnail(new_image)
                image.save(self.avatar.path)