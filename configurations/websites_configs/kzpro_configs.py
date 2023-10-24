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


# When you want to scrap a new website, use this template to configure all the website specific parameters and variables

website_key = "KZPRO" # change this
hebrew_name = "כלי זמר פרו"
english_name = "KZ-PRO"
base_url = "https://www.kzpro.co.il/" # make sure this ends with '/'
item_tag = "div" # example
item_class = "item_details" # example
name_tag = "h2"
name_class = None
upperprice_tag = "span"
upperprice_class = "oldprice"
lowerprice_tag = "span"
lowerprice_class = "saleprice"
lowerprice_css_class = "span.saleprice"

img_source = base64_imgs['kzpro']

method = vs.dynamic_method


main_html_tag = None
main_html_class = None

# update the below for websites that are using pagination (and not scroll) to load products

# try to scrap the pagination bar:
pagination_container_tag = "ul"
pagination_container_class = "pagination"
pagination_item_tag = "li"
pagination_item_class = "numbers"

paginate = vs.url_query_indicator + "bscrp=" + vs.page_index



""" When you finished don't forget to add the new website you've configs to websites_dict """

# Don't change the following except the script that should be updated after finish writing it

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