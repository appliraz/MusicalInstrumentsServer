import sys
import os
from os.path import dirname, abspath
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
grandparent_dir = dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

import variablesService as vs
from .websites_logos.base64_logos import base64_imgs


website_key = "MUSIC-CENTER"
hebrew_name = "מיוזיק סנטר"
english_name = "Music Center"
base_url = "https://www.music-center.co.il/"
item_tag = "div"
item_class = "grid row"
name_tag = "h3"
name_class = "title text-center"
upperprice_tag = "span" 
upperprice_class = "origin_price"
lowerprice_tag = "span"
lowerprice_class = "price"
lowerprice_css_class = "span.price"
img_source = base64_imgs['music-center']
#"https://drive.google.com/uc?export=view&id=1iv8hNHQaC-TaijZOPlb3nmmy_8muNE3O"

method = vs.selenium_method
main_html_tag = None
main_html_class = None

""" When you finished don't forget to add the new website you've configs to websites_dict """

# Don't change the following

website_configs = vs.getWebsiteConfigs()
website_configs[vs.website_url] = base_url
website_configs[vs.product_element]['tag'] = item_tag
website_configs[vs.product_element]['class'] = item_class
website_configs[vs.product_name]['tag'] = name_tag
website_configs[vs.product_name]['class'] = name_class
website_configs[vs.product_list_price]['tag'] = upperprice_tag
website_configs[vs.product_list_price]['class'] = upperprice_class
website_configs[vs.product_price]['tag'] = lowerprice_tag
website_configs[vs.product_price]['class'] = lowerprice_class
website_configs[vs.product_price]['css_class'] = lowerprice_css_class
website_configs[vs.hebrew_name] = hebrew_name
website_configs[vs.english_name] = english_name
website_configs[vs.logo_src] = img_source
website_configs[vs.method] = method
website_configs[vs.main_html_element]['tag'] = main_html_tag
website_configs[vs.main_html_element]['class'] = main_html_class