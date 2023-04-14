from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to='blog/images/')
    blog_date = models.DateField()
