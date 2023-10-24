""" Add parent package to project path """
import sys
import os
from os.path import dirname, abspath
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(current_dir)
sys.path.append(parent_dir)

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

from configurations import variablesService as vs
import ProductPageScrap

def getRelevantSoup(soup: BeautifulSoup, website_configs: dict):
    main_website_tag = website_configs[vs.main_html_element]['tag']
    main_website_class = website_configs[vs.main_html_element]['class']
    if(not main_website_tag or not main_website_class):
        return soup
    try:
        soup = soup.find(main_website_tag, class_ = main_website_class)
    except Exception as e:
        print(e)
    return soup


def parseSoup(soup: BeautifulSoup, website_configs: dict):
    try:
        soup = getRelevantSoup(soup, website_configs) #if necessary, gets the main page element from the soup
        data = getDataConcurrently(soup, website_configs)
        return data
    except Exception as e:
        print(e)
        raise Exception(e)

def getData(soup: BeautifulSoup, website: dict):
    data = []
    items = getItems(soup, website)
    for item in items:
        item_data = extractParameters(item, website) # contains link, name, price
        data.append(item_data)
    return data

def getDataConcurrently(soup: BeautifulSoup, website: dict):
    data = []
    items = getItems(soup, website)
    if not items:
        return []
    try:
        with ThreadPoolExecutor() as executor:
            futures = []
            for item in items:
                future = executor.submit(extractParameters, item, website)
                futures.append(future)
            for future in as_completed(futures):
                item_data = future.result()
                data.append(item_data)
        return data
    except Exception as e:
        print("exception in trying to getDataConcurrently")
        print(e)
        return []

def extractParameters(item: BeautifulSoup, website: dict):
    link = getLink(item, website)
    name = getName(item, website)
    print(f"product name is {name}")
    price = getPrice(item, website)
    upperprice, lowerprice = price if price else (None, None)
    if (lowerprice == vs.no_price_found or lowerprice == "" or lowerprice == None) and not upperprice:
        product_price = getPriceFromProductPage(link, website)
        price = product_price if product_price is not None else price
    return (link, name, price)
  
    
def getItems(soup: BeautifulSoup, website: dict):
    items_tag = website[vs.product_element]['tag']
    items_class = website[vs.product_element]['class']
    try:
        items = soup.find_all(items_tag, class_ = items_class)
    except Exception as e:
        print(f"could not find items by the provided items tag and class:\n{items_tag} {items_class}\ncheck exception below, returning empty array")
        print(e)
        items = []
    return items

def getParameter(item: BeautifulSoup, website: dict, param: str, value_if_error=None):
    print("\ngetParameter called\n")
    try:
        element = findElement(item, website, param)
        if param == vs.product_price:
            print(f"elemenet contents = {len(element.contents)}")
        param_text = getTextFromElement(element, param)
        if param == vs.product_price:
            print(f"found element: {element}\n\n\n")
    except Exception as e:
        print(e)
        param_text = value_if_error
    return param_text
    

""" Parameters Specific Functions """

def getLink(item: BeautifulSoup, website: dict):
    try:
        extension = item.find('a')['href'] if not item.name == 'a' else item['href']
        extension = cleanupLink(extension)
        link = addBaseUrlToLink(extension, website)
    except Exception as e:
        print(e)
        link = vs.no_link_found
    return link

def getName(item: BeautifulSoup, website: dict):
    name_text = getParameter(item, website, param=vs.product_name, value_if_error=vs.no_name_found)
    return name_text


def getUpperPrice(item: BeautifulSoup, website: dict):
    upperprice_text = getParameter(item, website, param=vs.product_list_price)
    return upperprice_text

def getLowerPrice(item: BeautifulSoup, website: dict):
    if item.find('del') and item.find('ins'): # avoid getting the 'upper price' usually within 'del' tag
        item = item.find('ins')
    lowerprice_text = getParameter(item, website, param=vs.product_price)
    return lowerprice_text

def getPrice(item: BeautifulSoup, website: dict):
    upperprice, lowerprice = extractUpperLowerPrice(item, website)
    if (lowerprice == vs.no_price_found or not lowerprice) and not upperprice:
        upperprice, lowerprice = getPriceFromProductPage(item, website)
    price = determineUpperLowerPrice(upperprice, lowerprice)
    return price

def extractUpperLowerPrice(item: BeautifulSoup, website: dict):
    upperprice = cleanupPrice(getUpperPrice(item, website))
    lowerprice = cleanupPrice(getLowerPrice(item, website))
    return (upperprice, lowerprice)

def determineUpperLowerPrice(upperprice, lowerprice):
    #if lowerprice exist, determine upper-lower price order
    if lowerprice:
        return (upperprice, lowerprice)
    #if only upper exist, deteremine it as the lower
    if not lowerprice and upperprice:
        return (lowerprice, upperprice)
    #if none exist return none found
    return (None, vs.no_price_found)


""" Utility Functions """

def findElement(item: BeautifulSoup, website: dict, param: str):
    param_tag = website[param]['tag']
    param_class = website[param]['class']
    elem = findElementByTagClass(item, param_tag, param_class)
    if not elem is None:
        return elem
    param_css_class = website[param]['css_class']
    elem = findElementByCssClass(item, param_css_class)
    return elem


def findElementByCssClass(item: BeautifulSoup, elem_css_class: str):
    if elem_css_class is None:
        return None
    return item.select(elem_css_class)


def findElementByTagClass(element: BeautifulSoup, elem_tag, elem_class=None):
    try:
        elem = element.find(elem_tag) if elem_class is None else element.find(elem_tag, class_ = elem_class)
    except Exception as e:
        print(e)
        elem = None
    return elem

def getTextFromElement(elem: BeautifulSoup, param: str):
    # lower-price elements usually contained within the contents of the price tag, otherwise it can be extract from the tag text
    if param == vs.product_price and len(elem.contents) > 1:
        return getTextUsingContents(elem)
    return elem.get_text(strip=True)


def getTextUsingContents(elem: BeautifulSoup):
    for i in range(len(elem.contents)):
        text = elem.contents[i]
        print(f"text is {text}")
        price = cleanupPrice(text)
        if not price:
            continue
        print(f"price is {price} in content no {i}")
        return price
    return None
    """
    elem_position = 2
    found = False
    text = None
    while not found and elem_position >= 0:
        try:
            text = elem.contents[elem_position]
            found = True
        except Exception as e:
            print(e)
        elem_position -= 1
    return text
    """

def cleanupPrice(price: str):
    if price is None or not isinstance(price, str):
        return price
    clean_price = ""
    for char in price:
        if char.isdigit():
            clean_price += char
    return clean_price

def cleanupLink(link: str):
    return link.lstrip('_ /').rstrip(' \n')

def addBaseUrlToLink(link: str, website: dict):
    base_url = website[vs.website_url]
    if base_url in link or base_url.replace("www.", "") in link:
        base_url = ""
    full_link = base_url + link
    return full_link

def getPriceFromProductPage(item_soup: BeautifulSoup, website:dict):
    try:
        product_url = getLink(item_soup, website)
        item = ProductPageScrap.initSoup(product_url)
        price = extractUpperLowerPrice(item, website)
        return price
    except Exception as e:
        print(e)
        return (None, vs.no_price_found)
    
# function relevant only for pagination websites
def getLastPage(first_page_soup: BeautifulSoup, website_configs: dict):
    print(website_configs)
    container_tag = website_configs[vs.pagination]['container']['tag']
    container_class = website_configs[vs.pagination]['container']['class']
    pagination_bar = first_page_soup.find(container_tag, class_ = container_class)
    print("pagination bar")
    print(pagination_bar)
    if pagination_bar is None:
        return 1
    item_tag = website_configs[vs.pagination]['item']['tag']
    item_class = website_configs[vs.pagination]['item']['class']
    pagination_items = pagination_bar.find_all(item_tag, class_ = item_class)
    last_page = -1
    for item in pagination_items:
        try:
            page_number = int(cleanupPrice(item.get_text(strip= True)))
        except Exception as e:
            print(e)
            continue
        if page_number > last_page:
            last_page = page_number
    if last_page == -1:
        last_page = vs.max_pages
    return last_page

