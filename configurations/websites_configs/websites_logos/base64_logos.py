import base64
import os
current_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
imgs_location = 'websites_logos_src/'


websites_imgs = {
    'kley-zemer': 'kley-zemer_logo.png',
    'avi-gil': 'avigil-logo.png',
    'diez': 'diez_logo.png',
    'halilit': 'halilit_logo.png',
    'music-center': 'music-center_logo.png',
    'wild-guitars': 'wildguitars-logo.png',
    'kzpro': 'Logo_KZPro.png'
}

base64_imgs = {}

for website_key, website_img in websites_imgs.items():
    img_path = imgs_location + website_img
    abs_img_path = os.path.join(current_dir, img_path)
    with open(abs_img_path, 'rb') as img_file:
        base64_imgs[website_key] = base64.b64encode(img_file.read()).decode('utf-8')



