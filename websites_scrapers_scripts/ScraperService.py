""" Add parent package to project path """
import sys
import os
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

from configurations.websites_configs.websites_dict import websites_dict
from configurations import variablesService as vs
from scrap_scripts import SoupParser, SeleniumScrap, PaginationScrap

def extractDomain(url: str):
    domain = url.replace("https://", "").replace("www.", "")
    return domain

def getWebsiteKey(url):
    for key, website_configs in websites_dict.items():
        domain = extractDomain(website_configs[vs.website_url])
        if domain in url:
            return key
    return None

""" Mendatory to name the main scrapping function 'scrap' """
def scrap(url):
    key = getWebsiteKey(url)
    print(f"key is {key}\n\n\n\n\n")
    website_configs = websites_dict[key]
    scraping_method = website_configs[vs.method]
    print(f'scraping method is {scraping_method}')
    soup = SeleniumScrap.initSoup(url) if scraping_method == vs.selenium_method else PaginationScrap.initSoup(url, website_configs)
    print("returned with soup")
    data = SoupParser.parseSoup(soup, website_configs)
    return data

"""
if __name__ == "__main__":
    scrap("https://www.halilit.com/23604-Studio-Monitors/33102-Mackie")
    print("END")
"""