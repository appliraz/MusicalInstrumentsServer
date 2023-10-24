from configurations.websites_configs.websites_dict import websites_dict
from configurations import variablesService as vs
from openpyxl import Workbook
from ExcelHandler import getDataAsExcelFileStream
from concurrent.futures import ThreadPoolExecutor, as_completed
from websites_scrapers_scripts.ScraperService import scrap

""" This module handles the connection between the flask server and the backend as in calling the relevant scraper script and writing to a file"""

def getAllowedWebsites():
    allowed = {}
    for website_key in websites_dict:
        website_params = websites_dict[website_key]
        website = {}
        website['address'] = website_params[vs.website_url]
        website['english_name'] = website_params[vs.english_name]
        website['hebrew_name'] = website_params[vs.hebrew_name]
        website['img_src'] = website_params[vs.logo_src]
        allowed[website_key] = website
    return allowed


def getWebsiteConfigs(url):
    print(f"finding the relevant scraper for url {url}")
    for website_key in websites_dict:
        website_params = websites_dict[website_key]
        website_url = website_params[vs.website_url]
        if website_url in url or website_url.replace("www.", "") in url:
             return website_params
    return Exception("This url doesn't seems to have a supported website")


def getScrapedData(url: str, website_configs: dict):
    print('started the scraping')
    try:
        data = scrap(url)
        return data
    except Exception as e:
        print("Failed in scraping data, sending empty array\n")
        print(e)
        raise Exception("Unsuccessful scrap")
    
def doScraping(url: str):
    try:
        scraper_configs = getWebsiteConfigs(url)
        scraped_data = getScrapedData(url, scraper_configs)
        scraped_data_name = scraper_configs[vs.english_name]
        return(scraped_data, scraped_data_name)
    except Exception as e:
        print(e)
        return None


def scrapToExcel(urls: list, filename="TheMusicalInstrumentsScraper"):
    print('start scraping')
    if not urls:
        raise Exception("No URLs received")
    complete_scrap = []
    for url in urls:
        try:
            scraper_configs = getWebsiteConfigs(url)
            scraped_data = getScrapedData(url, scraper_configs)
            scraped_data_name = scraper_configs[vs.english_name]
            complete_scrap.append((scraped_data, scraped_data_name))
        except Exception as e:
            print(e)
            continue
    filestream = getDataAsExcelFileStream(complete_scrap)
    return filestream

def scrapToExcelConcurrently(urls: list, filename="TheMusicalInstrumentsScraper"):
    print('start scraping')
    if not urls:
        raise Exception("No URLs received")
    complete_scrap_results = []
    with ThreadPoolExecutor() as executor:
        futures = []

        for url in urls:
            future = executor.submit(doScraping, url)
            futures.append(future)

        for future in as_completed(futures):
            result = future.result()
            complete_scrap_results.append(result)

    filestream = getDataAsExcelFileStream(complete_scrap_results)
    return filestream

#main(["https://www.halilit.com/23604-Studio-Monitors", "https://diez.co.il/product-category/%d7%a1%d7%90%d7%95%d7%a0%d7%93-%d7%95%d7%94%d7%92%d7%91%d7%a8%d7%94/%d7%90%d7%95%d7%9c%d7%a4%d7%9f/%d7%9e%d7%95%d7%a0%d7%99%d7%98%d7%95%d7%a8%d7%99%d7%9d-%d7%90%d7%95%d7%9c%d7%a4%d7%a0%d7%99%d7%99%d7%9d/"])