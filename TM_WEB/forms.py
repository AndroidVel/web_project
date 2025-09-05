from django import forms
from .models import ImageFeed, AudioFeed, ImageAudioFeed, AudioImageFeed


class ImageFeedForm(forms.ModelForm):
    class Meta:
        model = ImageFeed
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        help_texts = {
            'image': 'Upload an image file.',
        }


class AudioFeedForm(forms.ModelForm):
    class Meta:
        model = AudioFeed
        fields = ['audio']
        widgets = {
            'audio': forms.FileInput(attrs={'accept': 'audio/*'}),
        }
        help_texts = {
            'audio': 'Upload an audio file.',
        }

class ImageAudioFeedForm(forms.ModelForm):
    class Meta:
        model = ImageAudioFeed
        fields = ['image', 'audio']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
            'audio': forms.FileInput(attrs={'accept': 'audio/*'}),
        }
        help_texts = {
            'image': 'Upload an image file.',
            'audio': 'Upload an audio file.',
        }

class ImageToAudioFeedForm(forms.ModelForm):
    class Meta:
        model = AudioImageFeed
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        help_texts = {
            'image': 'Upload an image file.',
        }