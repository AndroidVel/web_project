from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# from .models import ImageFeed
# from .utils import process_image
# from .forms import ImageFeedForm


def home(request):
    return render(request, 'base.html')


def audio_to_image(request):
    return render(request, 'audio_to_image.html')


def image_to_audio(request):
    return render(request, 'image_to_audio.html')


@login_required
def audio_from_image(request):
    return redirect('TM_WEB:audio_from_image')


@login_required
def audio_insert_in_image(request):
    return render(request, 'audio_insert_in_image.html')


@login_required
def process_image_feed(request, feed_id):
    return redirect('TM_WEB:dashboard')

