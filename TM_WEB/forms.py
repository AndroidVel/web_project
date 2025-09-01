from django import forms
from .models import ImageFeed, AudioFeed


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