from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    images = models.ImageField(upload_to='projects/images/')
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.description


class About_Me(models.Model):
    about_images = models.ImageField(upload_to='about_me/images/')
    about_intro = models.TextField()
    about_p_one = models.TextField()
    about_p_two = models.TextField()
    about_name = models.CharField(max_length=100)
    about_location = models.CharField(max_length=100)
    about_loc_status = models.CharField(max_length=100)
    about_resume_pdf = models.FileField(upload_to='about_me/files/')

    def __str__(self):
        return self.about_name


class Education(models.Model):
    edu_images = models.ImageField(upload_to='edu_images/images')
    edu_url = models.URLField(blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=True)
    message = models.TextField()

    def __str__(self):
        return self.name
