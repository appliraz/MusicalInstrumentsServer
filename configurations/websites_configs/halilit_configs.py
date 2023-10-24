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



website_key = "HALILIT"
hebrew_name = "חלילית"
english_name = "Halilit"
base_url = "https://www.halilit.com/"
item_tag = "div"
item_class = "grid row border_grid max-width-responsive margin-responsive articles max-height-responsive"
name_tag = "h1"
name_class = None
upperprice_tag = "p"
upperprice_class = "origin_price line-through text-center"
lowerprice_tag = "span"
lowerprice_class = "price center-price-in-grid text-center" #center-price-in-grid text-center
lowerprice_css_class = "span.price.center-price-in-grid.text-center.center_price.PriceChecked"
img_source = base64_imgs['halilit']
#"https://drive.google.com/uc?export=view&id=1oB0IW0byTOZNOc2wwi06jijox1NdtwwA"

method = vs.selenium_method
main_html_tag = None
main_html_class = None

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
website_configs[vs.product_price]['css_class'] = lowerprice_class
website_configs[vs.hebrew_name] = hebrew_name
website_configs[vs.english_name] = english_name
website_configs[vs.logo_src] = img_source
website_configs[vs.method] = method
website_configs[vs.main_html_element]['tag'] = main_html_tag
website_configs[vs.main_html_element]['class'] = main_html_class