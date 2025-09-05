from django.db import models
from django.conf import settings


class ImageFeed(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    processed_to_audio = models.FileField(upload_to='audio/')

class AudioFeed(models.Model):
    name = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/')
    processed_to_image = models.ImageField(upload_to='images/')

class ImageAudioFeed(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    processed_image = models.ImageField(upload_to='images/')

class AudioImageFeed(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    processed_to_audio = models.FileField(upload_to='audio/')