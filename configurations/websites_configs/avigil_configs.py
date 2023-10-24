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


website_key = "AVIGIL" 
base_url = "https://www.avigil.co.il/" 
item_tag = "a" 
item_class = "prod_inner block"
name_tag = "span"
name_class = "prod_title block"
upperprice_tag = "del" 
upperprice_class = None
lowerprice_tag = "bdi"
lowerprice_class = None
lowerprice_css_class = "span.woocommerce-Price-amount.amount"
hebrew_name = "אבי גיל"
english_name = "Avi Gil"
img_source = base64_imgs['avi-gil']
#"https://drive.google.com/uc?export=view&id=1bUAxqLlJVpfie3lQK75Ae_FuS6O9MbsS"

method = vs.selenium_method

main_html_tag = "section"
main_html_class = "category_page"

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