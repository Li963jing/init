from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title  = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        blank=True, 
        null=True,
    )

    def __str__(self):
        return self.title    # admin中显示的title的名称

    def get_absolute_url(self):
        return reverse("post_detail",args=[str(self.id)])
        # 指的是：在创建提交后跳转到post_detail页面



class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options={'quality':100},
        blank=True, 
        null=True,   
    )