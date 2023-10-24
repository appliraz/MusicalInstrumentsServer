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


website_key = "DIEZ" 
base_url = "https://www.diez.co.il/"
item_tag = "a"
item_class = "woocommerce-LoopProduct-link woocommerce-loop-product__link"
name_tag = "h2"
name_class = "woocommerce-loop-product__title"
upperprice_tag = "del" 
upperprice_class = None
lowerprice_tag = "bdi"
lowerprice_class = None
lowerprice_css_class = "span.woocommerce-Price-amount.amount"
hebrew_name = "דיאז"
english_name = "Diez"
img_source = base64_imgs['diez']
#"https://drive.google.com/uc?export=view&id=1mMzbXMNLJtB9HA4pHKUzcGJfeY929Tph"

method = vs.pagination_method

main_html_tag = None
main_html_class = None


# try to scrap the pagination bar:
pagination_container_tag = "ul"
pagination_container_class = "page-numbers"
pagination_item_tag = "li"
pagination_item_class = None

paginate = vs.extension_indicator + "page/" + vs.page_index

""" ! When you finished don't forget to add the new website you've configs to websites_dict ! """

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
website_configs[vs.pagination]['container']['tag'] =  pagination_container_tag
website_configs[vs.pagination]['container']['class'] =  pagination_container_class
website_configs[vs.pagination]['item']['tag'] = pagination_item_tag
website_configs[vs.pagination]['item']['class'] = pagination_item_class
website_configs[vs.pagination]['indicator'] = paginate
website_configs[vs.hebrew_name] = hebrew_name
website_configs[vs.english_name] = english_name
website_configs[vs.logo_src] = img_source
website_configs[vs.method] = method
website_configs[vs.main_html_element]['tag'] = main_html_tag
website_configs[vs.main_html_element]['class'] = main_html_class