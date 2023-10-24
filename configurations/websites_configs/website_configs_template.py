import sys
import os
from os.path import dirname, abspath
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
grandparent_dir = dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

import variablesService as vs

# When you want to scrap a new website, use this template to configure all the website specific parameters and variables

website_key = "NAME_USED_TO_ACCESS_THE_CONFIGS" # change this
hebrew_name = ""
english_name = ""
base_url = "https://www.example.com/" # make sure this ends with '/'
item_tag = "div" # example
item_class = "grid row border_grid max-width-responsive margin-responsive articles max-height-responsive" # example
name_tag = ""
name_class = ""
upperprice_tag = "" 
upperprice_class = "" # if not exist enter None
lowerprice_tag = ""
lowerprice_class = ""
lowerprice_css_class = ""
img_source = "" # use an image url path

method = "" # use vs.dynamic_method or vs.selenium_method or vs.pagination_method

main_html_tag = None
main_html_class = None

# update the below for websites that are using pagination (and not scroll) to load products

# try to scrap the pagination bar:
pagination_container_tag = ""
pagination_container_class = ""
pagination_item_tag = ""
pagination_item_class = ""

# here you have to follow this rules: start either with:
#  "?" (for pagination as parampeter in a url query) 
#  "/" (for pagination as extension to the url)
# in the string where the actual page number goes replace with <pg>
# please refer to the variablesService to see the actual signs used for "?", "/", "<pg>"

paginate = vs.url_query_indicator + "page=" + vs.page_index # valid example

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