from django.urls import path

from .views import home, audio_to_image, image_to_audio, audio_from_image, audio_insert_in_image, process_image_feed

from django.conf import settings
from django.conf.urls.static import static
app_name = 'TM_WEB'

urlpatterns = [
    path('', home, name='home'),
    path('audio_to_image/', audio_to_image, name='audio_to_image'),
    path('image_to_audio/', image_to_audio, name='image_to_audio'),
    path('audio_from_image/', audio_from_image, name='audio_from_image'),
    path('audio_insert_in_image/', audio_insert_in_image, name='audio_insert_in_image'),
    path('process/<int:feed_id>/', process_image_feed, name='process_feed'),
    # path('add-image-feed/', add_image_feed, name='add_image_feed'),
    # path('image/delete/<int:image_id>/', delete_image, name='delete_image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
