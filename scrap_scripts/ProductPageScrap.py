import requests
from bs4 import BeautifulSoup

def requestUrl(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Error with url address\nstatus code = {res.status_code}\n{url}")
    return res

def initSoup(url):
    print("PRODUCT PAGE SCRAP CALLED")
    res = requestUrl(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup
