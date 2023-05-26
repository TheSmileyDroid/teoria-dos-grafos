import imageio
import os

def make_gif(folder, name):
    image_folder = './.tests'
    video_name = '.tests/animation.gif'

    images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
    images.sort()

    frames = []
    for i in images:
        frames.append(imageio.imread(os.path.join(image_folder, i)))

    imageio.mimsave(video_name, frames, duration = 1)
