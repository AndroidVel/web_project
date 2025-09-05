from django.shortcuts import render, get_object_or_404
from TM_WEB.forms import ImageFeedForm, AudioFeedForm, ImageAudioFeedForm, ImageToAudioFeedForm
from .models import AudioFeed, ImageFeed, ImageAudioFeed, AudioImageFeed
from .functions import audio_to_image as a_to_i, image_to_audio as i_to_a, image_and_audio_to_image as i_and_a_to_i
from .functions import audio_from_image as a_from_i


def home(request):
    return render(request, 'home.html')


def audio_to_image(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            image = get_object_or_404(AudioFeed, id=int(request.POST['delete']))
            image.delete()
        elif 'process' in request.POST:
            audio = AudioFeed.objects.get(id=int(request.POST['process']))
            audio.processed_to_image = a_to_i('../SiteforTM/media/' + audio.audio.name, audio.audio.name[6::])
            audio.save()

        else:
            print(request.FILES)
            form = AudioFeedForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES['audio'].name, type(request.FILES['audio'].name))
                audio_feed = form.save(commit=False)
                audio_feed.save()
                audio = AudioFeed.objects.last()
                audio.name = request.FILES['audio'].name
                audio.save()
    return render(request, 'audio_to_image.html', {'form': AudioFeedForm(), 'feeds': AudioFeed.objects.all()})


def image_to_audio(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            image = get_object_or_404(ImageFeed, id=int(request.POST['delete']))
            image.delete()
        elif 'process' in request.POST:
            image = ImageFeed.objects.get(id=int(request.POST['process']))
            image.processed_to_audio = i_to_a('../SiteforTM/media/' + image.image.name, image.image.name[7::])
            image.save()
        else:
            print(request.FILES)
            form = ImageFeedForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES['image'].name, type(request.FILES['image'].name))
                image_feed = form.save(commit=False)
                image_feed.save()
                image = ImageFeed.objects.last()
                image.name = request.FILES['image'].name
                image.save()

    return render(request, 'image_to_audio.html', {'form': ImageToAudioFeedForm(), 'feeds': ImageFeed.objects.all()})


def audio_insert_in_image(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            image = get_object_or_404(ImageAudioFeed, id=int(request.POST['delete']))
            image.delete()
        elif 'process' in request.POST:
            image = ImageAudioFeed.objects.get(id=int(request.POST['process']))
            quality = int(request.POST['quality'])
            image.processed_image.delete()
            image.processed_image = i_and_a_to_i('../SiteforTM/media/' + image.image.name, '../SiteforTM/media/' + image.audio.name,  image.name, quality)
            image.save()
        else:
            print(request.FILES)
            form = ImageAudioFeedForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES['image'].name, type(request.FILES['image'].name))
                image_feed = form.save(commit=False)
                image_feed.save()
                image = ImageAudioFeed.objects.last()
                image.name = f"{request.FILES['image'].name[:-4]}_{request.FILES['audio'].name[:-4]}"
                image.save()
    return render(request, 'audio_insert_in_image.html', {'form': ImageAudioFeedForm, 'feeds': ImageAudioFeed.objects.all()})


def audio_from_image(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            image = get_object_or_404(AudioImageFeed, id=int(request.POST['delete']))
            image.delete()
        elif 'process' in request.POST:
            image = AudioImageFeed.objects.get(id=int(request.POST['process']))
            image.processed_to_audio.delete()
            image.processed_to_audio = a_from_i('../SiteforTM/media/' + image.image.name, image.image.name[7::])
            image.save()
        else:
            print(request.FILES)
            form = ImageToAudioFeedForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES['image'].name, type(request.FILES['image'].name))
                image_feed = form.save(commit=False)
                image_feed.save()
                image = AudioImageFeed.objects.last()
                image.name = request.FILES['image'].name
                image.save()
    return render(request, 'audio_from_image.html', {'form': ImageToAudioFeedForm, 'feeds': AudioImageFeed.objects.all()})

