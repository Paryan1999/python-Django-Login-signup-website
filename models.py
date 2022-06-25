from django.db import models

# Create your models here.


class Blog(models.Model):
    blog_heading = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='blog_images')
    blog_desc = models.TextField(max_length=1500)
    pub_date = models.DateTimeField(auto_now_add=True)
    publicer_name = models.CharField(max_length=50)


class Profile(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=1200)
    p_img=models.ImageField(upload_to='images')
