from django.db import models
from django.conf import settings


class ImageFeed(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_to_audio = models.FileField(upload_to='audio/')

class AudioFeed(models.Model):
    audio = models.FileField(upload_to='audio/')
    processed_to_image = models.ImageField(upload_to='images/')

class ImageAudioFeed(models.Model):
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    processed_image = models.ImageField(upload_to='images/')

class AudioImageFeed(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_to_audio = models.FileField(upload_to='audio/')