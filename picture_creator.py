import requests
import json
from parser import find_needed_line, delimiter
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
from urllib.request import urlopen
from classes import Images
from pathlib import Path

path = Path('images/default_background.jpg')


def find_images(id_number):
    res = requests.get('https://www.strava.com/challenges/' + str(id_number))
    all_inform = res.text

    if 'data-react-props=' in all_inform:
        pre_json = find_needed_line(delimiter(all_inform))
        json_file = pre_json.replace('&quot;', '"')
        final_json = json.loads(json_file)
        images = Images(final_json)
        background_link = images.background
        logo_link = images.logo
        return background_link, logo_link
    else:
        all_inform_list = all_inform.split('\n')
        for i in all_inform_list:
            if '<img alt=' in i:
                current_list = i.split()
                for j in current_list:
                    if 'src="' in j:
                        str_with_link = j
                        logo_link = str_with_link.strip('src=">')
                        background_link = 'no image'
                        return background_link, logo_link


def image_maker(link_tuple):
    background_link, logo_link = link_tuple
    needed_width = 1200
    needed_height = 600
    needed_ratio = needed_width / needed_height
    if background_link == 'no image':
        background = Image.open(path)
    else:
        background = Image.open(urlopen(background_link)).convert('RGB')
        width, height = background.size
        picture_ratio = width / height
        if needed_ratio > picture_ratio:
            background = crop_center(background, width, width // 2)
        elif needed_ratio <= picture_ratio:
            background = crop_center(background, height * 2, height)

    logo = Image.open(urlopen(logo_link))

    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.8)
    background = background.resize((needed_width, needed_height), Image.ANTIALIAS)
    logo = logo.resize((250, 250), Image.ANTIALIAS).convert('RGBA')

    transparent = Image.new('RGBA', (needed_width, needed_height), (0, 0, 0, 0))
    transparent.paste(background, (0, 0))
    transparent.paste(logo, (50, 300), mask=logo)
    return transparent


def crop_center(pil_img, crop_width: int, crop_height: int):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def get_bytes_from_image(image):
    img_bytes = BytesIO()
    img_bytes.name = 'image.png'
    image.save(img_bytes, 'PNG')
    img_bytes.seek(0)
    return img_bytes
