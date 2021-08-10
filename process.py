import cv2
from PIL import Image

ASCII_CHARS = ['@', '#', '$', '%', '?', '*', '+', ';', ':', ',', '.']

def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=150):
    image = image.convert('L')
    image = resize(image, new_width)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def process(image, width=100):
    res = do(image, width)
    return res

def video(video, size = 40):
    all_frames = []
    cap = cv2.VideoCapture(video)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            all_frames.append(process(Image.fromarray(frame), size))
        else:
            break
    cap.release()

    return all_frames