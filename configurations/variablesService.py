# Product Parameters / Properties 
product_element = 'item'
product_name = 'name'
product_list_price = 'upperprice'
product_price = 'lowerprice'
pagination = 'pagination'
script = 'script'
hebrew_name = 'hebrew_name'
english_name = 'english_name'
logo_src = 'img_src'
website_url = 'website_url'
main_html_element = 'main_html_element'

# Scrap Method
method = 'method'
pagination_method = 'pagination'
dynamic_method = 'dynamic'
selenium_method = 'selenium'


# Selenium Scrapers
max_scrolls = 18

# Pagination Scrapers
url_query_indicator = "?"
url_param = "&"
extension_indicator = "/"
max_pages = 20
page_index = "<pg>" #the number of the page as it's a dynamic value that changes from page to page
method_requests = "requests"
method_selemiun = "selemium"
dynamic = "dyamic"
static = "static"

# Parsing
parse_by_strip = "strip"
parse_by_contents = "contents"


# Errors
no_link_found = "no link"
no_name_found = "no name"
no_price_found = "no price"

# EXCEL
link_header = 'Product URL'
name_header = 'Product Model Name'
price_header = 'Product Price'



price_bad_chars = [' ', ',', '₪']

# Configuration File
def getWebsiteConfigs():
    website_configurations = {
        website_url: "",
        product_element: {"tag": "", "class": ""},
        product_name: {"tag": "", "class": ""},
        product_list_price: {"tag": "", "class": ""},
        product_price: {"tag": "", "class": "", "css_class": ""},
        method: "",
        pagination: {"indicator": "", "container": {"tag": "", "class": ""}, "item": {"tag": "", "class": ""}},
        hebrew_name: "",
        english_name: "",
        logo_src: "",
        main_html_element: {"tag": None, "class": None}
    }
    return website_configurations