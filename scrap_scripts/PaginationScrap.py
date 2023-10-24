""" Add parent package to project path """
import sys
import os
from os.path import dirname, abspath
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(current_dir)
sys.path.append(parent_dir)


#print(sys.path)

""" Import extrnal packages """
from bs4 import BeautifulSoup
import requests


""" Import project modules """
from configurations import variablesService as vs
from ChromeDriverService import getSeleniumDriver, isWebdriver
import SoupParser


def getTextToScrap(loader, url: str, first_page: int, website_configs: dict) -> str:
    page = first_page
    current_url = getNextUrl(url, page)
    res = requestUrl(loader, current_url)
    scrap_text = ""
    first_page_text = getTextFromResponse(loader, res)
    last_page = getLastPageFromText(first_page_text, website_configs)
    while page <= last_page and isStatusCodeOK(current_url):
        print(f"page = {page}")
        page_text = getTextFromResponse(loader, res)
        if not page_text:
            break
        scrap_text += page_text
        print("\nscrap_text\n")
        page += 1
        current_url = getNextUrl(url, page)
        try:
            res = requestUrl(loader, current_url)
        except Exception as e:
            print(e)
            break
    return scrap_text

def getPageLoader(method):
    if method==vs.pagination_method:
        return requests.Session()
    elif method==vs.dynamic_method:
        return getSeleniumDriver()
    else:
        raise Exception(f"Unknown method for page loader in getPageLoader(), method = {method}")

def closePageLoader(method, loader):
    if method==vs.pagination_method:
        loader.close()
    elif method==vs.dynamic_method:
        loader.quit()
    else:
        raise Exception(f"Unknown method for page loader in getPageLoader(), method = {method}")    

def getSoup(url: str, first_page: int, website_configs: dict, method):
    loader = getPageLoader(method)
    scrap_text = getTextToScrap(loader, url, first_page, website_configs)
    closePageLoader(method, loader)
    if not scrap_text:
        raise Exception("Something went wrong and no text was found")
    full_bowl_of_soup = BeautifulSoup(scrap_text, 'html.parser')
    return full_bowl_of_soup



def paginateUrl(url: str, website_configs: dict):
    print(website_configs)
    website_pagination = website_configs[vs.pagination]['indicator']
    if vs.page_index not in website_pagination:
        raise Exception(f"The configuration for website_pagination is invalid\nThe website_pagination has to contain {vs.page_index}, found: {website_pagination}")
    if isPaginationApplied(url, website_pagination):
        fixed_url, first_page = addPageIndexToUrl(url, website_pagination)
        return fixed_url, first_page
    if vs.url_query_indicator in website_pagination:
        paginate_url = appendQueryToUrl(url, website_pagination)
        first_page = 1
        return paginate_url, first_page
    if vs.extension_indicator in website_pagination:
        paginate_url = appendExtensionToUrl(url, website_pagination)
        first_page = 1
        return paginate_url, first_page
    raise Exception(f"The configuration for website_pagination is invalid\nExcpected to have {vs.url_query_indicator} or {vs.extension_indicator} but none were found in {website_pagination}")


def initSoup(url: str, website_configs: dict):
    paginate_url, first_page = paginateUrl(url, website_configs)
    print("\n\tpaginated")
    print(paginate_url)
    method= website_configs[vs.method]
    soup = getSoup(paginate_url, first_page, website_configs, method)
    return soup

    



""" Utility Functions """

def appendQueryToUrl(url: str, website_pagination: str):
    if vs.url_query_indicator in url:
        website_pagination = website_pagination.replace(vs.url_query_indicator, vs.url_param)
    url = removeLastExtensionSign(url)
    url += website_pagination
    return url

def removeLastExtensionSign(url: str):
    if url[-1] == vs.extension_indicator:
        url = url[:-1]
    return url

def addExtensionAtIndex(url: str, extension: str, index: int):
    left_url = url[:index]
    right_url = url[index:]
    left_url = removeLastExtensionSign(left_url)
    url = left_url + extension + right_url
    return url

def appendExtensionToUrl(url: str, website_pagination: str):
    if vs.url_query_indicator in url:
        query_index = url.find(vs.url_query_indicator)
        url = addExtensionAtIndex(url, extension=website_pagination, index=query_index)
    else:
        url = removeLastExtensionSign(url)
        url += website_pagination
    return url

def getNextUrl(url: str, page: int):
    next_url = url.replace(vs.page_index, str(page))
    return next_url

def isPaginationApplied(url: str, pagination: str):
    indicator = pagination.replace(vs.page_index, "")
    return indicator in url or indicator[1:] in url

def addPageIndexToUrl(url: str, website_pagination: str):
    page_index = vs.page_index
    paginate = website_pagination.replace(page_index, "")
    index = url.find(paginate)
    left_url = url[:index+len(paginate)]
    right_url = url[len(left_url):]
    end_of_page_number_index = getNextSignIndex(right_url)
    current_page = right_url[:end_of_page_number_index]
    right_url = right_url[end_of_page_number_index:]
    full_url = left_url + vs.page_index + right_url
    return (full_url, int(current_page))

def getNextSignIndex(url: str):
    signs = [vs.url_query_indicator, vs.extension_indicator, ",", vs.url_param]
    next_index = len(url)
    for sign in signs:
        index =  url.find(sign)
        if index != -1 and index < next_index:
            next_index = index
    return next_index

def getTextFromResponse(loader, response):
    try:
        text = ""
        if type(loader)==requests.Session:
            text = response.text
        elif isWebdriver(loader):
            text = loader.page_source
        else:
            raise Exception("Unkown type for loader")
        return text
    except Exception as e:
        print(e)
        return ""

def requestUrl(session: requests.Session, url: str) -> requests.Response:
    r = session.get(url)
    return r

def getLastPage(first_page_res, website_configs: dict):
    if first_page_res.status_code != 200:
        return vs.max_pages
    page_soup = BeautifulSoup(first_page_res.text, "html.parser")
    try:
        last_page = SoupParser.getLastPage(page_soup, website_configs)
        print(f"\nlast page is : {last_page}")
        return last_page
    except Exception as e:
        print(e)
        return vs.max_pages
    
def getLastPageFromText(page_text: str, website_configs:dict):
    try:
        page_soup = BeautifulSoup(page_text, "html.parser")
        last_page = SoupParser.getLastPage(page_soup, website_configs)
        print(f"\nlast page is : {last_page}")
        return last_page
    except Exception as e:
        print(e)
        return vs.max_pages
    
def isStatusCodeOK(url):
    return requests.get(url).status_code == 200