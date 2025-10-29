import wave
import warnings

from scipy.io.wavfile import write, read
import numpy as np
from PIL import Image
import math
import imageio.v3 as imageio


def audio_to_image(audio_file, filename):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        file = read(audio_file)


    max_number = max(abs(file[1]))
    if max_number > 1:
        transpose_rate = (2 ** 31 - 1) // np.float32(max_number)
    else:
        transpose_rate = 2 ** 31-1
    audio = np.array(file[1] * transpose_rate, dtype=np.int64)
    print(audio)
    width = round(math.sqrt(len(audio)))
    print('1:', audio)
    audio = np.append(audio, np.zeros(abs(len(audio) - width ** 2), dtype=np.int32))
    print('2:', audio)
    audio = np.uint32(audio)
    print('3:', audio)
    im = Image.fromarray(audio.reshape(int(len(audio) / width), width), mode='RGBA')
    im.save(f'media/images/{filename[:-4]}.png')
    print(np.array(im))
    return f'images/{filename[:-4]}.png'


def to_audio(a):
    return np.int32(a[0]) + np.int32(a[1]) * 2 ** 8 + np.int32(a[2]) * 2 ** 16 + np.int32(a[3]) * 2 ** 24

def image_to_audio(image_file, filename):
    file = imageio.imread(image_file)
    print(file, file.shape, file.dtype, file.size)
    data = np.array(file, dtype=np.int32)

    data = np.reshape(data, (np.size(data) // 4, 4))
    wavfile = np.apply_along_axis(to_audio, 1, data)
    write(f'media/audio/{filename[:-4]}.wav', 44100, wavfile)
    return f'audio/{filename[:-4]}.wav'


def image_and_audio_to_image(image_file, audio_file, filename, quality):
    data_i = imageio.imread(image_file)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        audio = read(audio_file)
    shape = data_i.shape
    # data_i = np.reshape(image, (np.size(image) // 4, 4))
    # data_i = np.delete(image, np.s_[3::4], 1)
    print('1:', data_i)
    # print(data_i.shape, data_i.dtype, data_i.size, data_i)
    transpose_rate = quality / max(abs(audio[1]))
    print(transpose_rate, max(abs(audio[1])))
    data_a = np.array(audio[1] * transpose_rate - quality - 1, dtype=np.uint8)
    data_a = np.insert(data_a, 0, quality)
    print(data_a, '_______________________________________________________________________')
    if len(data_a) < np.size(data_i) // 3:
        data_i = np.resize(data_i, np.size(data_i))
        data_a = np.append(data_a, np.ones(np.size(data_i) // 3 - len(data_a), dtype=np.uint8) * 255)
        print(data_i, len(data_a), len(data_i) // 3)
    else:
        data_a = np.delete(data_a, np.s_[np.size(data_i) // 3:len(data_a)], 0)
    data_a = np.reshape(data_a, (np.size(data_a), 1))
    data_i = np.reshape(data_i, (np.size(data_i) // 3, 3))
    print(data_a, data_i.dtype, data_a.dtype)
    data = np.concatenate((data_i, data_a), axis=1)
    print(data.reshape((shape[0], shape[1], 4)))
    im = Image.fromarray(data.reshape((shape[0], shape[1], 4)), mode='RGBA')
    print(np.array(im))
    print(max(data_a), min(data_a))
    print('QUALITY:', quality)
    im.save(f'media/images/{filename}.png')
    return f'images/{filename}.png'


def audio_from_image(image_file, filename):
    file = imageio.imread(image_file)
    print(file)
    data = np.reshape(file, np.size(file))
    print('______________________________________________________________________')
    print(data)
    data = np.delete(data, np.s_[::4], 0)
    print('______________________________________________________________________')
    print(data)
    data = np.delete(data, np.s_[::3], 0)
    print('______________________________________________________________________')
    print(data)
    data = np.delete(data, np.s_[::2], 0)
    print('______________________________________________________________________')
    print(data)
    data = np.reshape(data, np.size(data))
    quality = np.take(data, 0, 0)
    data = np.delete(data, 0, 0)
    print(max(data), min(data))
    data= np.array(data, dtype=np.int16)
    data = np.array((data - min(data) - (max(data) - min(data)) // 2) * (2 ** 14 // np.int16(quality)-1))
    print(data)
    print('QUALITY:', quality)
    write(f'media/audio/{filename[:-4]}.wav', 44100, data)
    return f'audio/{filename[:-4]}.wav'