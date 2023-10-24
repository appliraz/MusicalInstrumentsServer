from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
#from flaskscraper import getChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager



def getChromeOptions():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Enable headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (may be required in some cases)
    return chrome_options

chrome_driver = ChromeDriverManager().install()
chrome_options = getChromeOptions()

def getSeleniumDriver():
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    #driver = webdriver.Chrome(chrome_driver)
    return driver

"""
def getSeleniumDriver():
    chrome_options = getChromeOptions()
    driver = webdriver.Chrome(getChromeDriverManager(), options=chrome_options)
    return driver
"""

def isWebdriver(loader):
    return type(loader) == webdriver.Chrome





