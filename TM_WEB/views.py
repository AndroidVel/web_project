from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from TM_WEB.forms import ImageFeedForm, AudioFeedForm
from .models import AudioFeed
from .functions import audio_to_image as a_to_i
# from .models import ImageFeed
# from .utils import process_image
# from .forms import ImageFeedForm


def home(request):
    return render(request, 'home.html')


def audio_to_image(request):
    if request.method == 'POST':
        print(request.FILES)
        form = AudioFeedForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['audio'].name)
            audio_feed = form.save(commit=False)
            audio_feed.save()
            audio = AudioFeed.objects.get(audio='audio/' + request.FILES['audio'].name)
            audio.processed_to_image = a_to_i('../SiteforTM/media/audio/' + request.FILES['audio'].name, request.FILES['audio'].name)
            print(AudioFeed.objects.get(audio='audio/' + request.FILES['audio'].name))
            audio.save()

    else:
        form = AudioFeedForm()
    feeds = AudioFeed.objects.all()
    print([f.audio.url for f in feeds])
    return render(request, 'audio_to_image.html', {'form': form, 'feeds': feeds})


def image_to_audio(request):
    return render(request, 'image_to_audio.html')


@login_required
def audio_from_image(request):
    return render(request, 'audio_from_image.html')


@login_required
def audio_insert_in_image(request):
    return render(request, 'audio_insert_in_image.html')


@login_required
def process_image_feed(request, feed_id):
    return render(request, 'process_image_feed.html')

