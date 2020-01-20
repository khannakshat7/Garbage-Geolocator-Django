from django.db import models

# Create your models here.

class garbage_report(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_url

class potholes_report(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_url

class cattles_report(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_url