""" Add parent package to project path """
import sys
import os
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

""" Import extrnal packages """
from selenium import webdriver
from bs4 import BeautifulSoup
import time


""" Import project modules """
from configurations import variablesService
from ChromeDriverService import getSeleniumDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains






def scrollToTheBottom(driver: webdriver.Chrome):
    last_height = driver.execute_script("return document.body.scrollHeight")
    move_mouse_to_center(driver)
    max_scrolls = variablesService.max_scrolls
    current_scroll = 0
    while True and current_scroll<max_scrolls:
        print("scroll")
        driver.execute_script(f"window.scrollTo(0, {last_height*0.8});")
        # Wait for the page to load
        time.sleep(4)
        # Get the new height of the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # If the page height hasn't changed, we've reached the end of the page
        if new_height == last_height and current_scroll > 2:
            break
        
        last_height = new_height
        current_scroll += 1
    
def getSoup(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup


def initSoup(url, use_scroll=True):
    driver = getSeleniumDriver()
    driver.get(url)
    if use_scroll:
     scrollToTheBottom(driver)
    soup = getSoup(driver)
    return soup




def move_mouse_to_center(driver: webdriver.Chrome):
    try:
        center_element = driver.find_element(By.TAG_NAME, 'body')
        action_chains = ActionChains(driver)
        action_chains.move_to_element(center_element).perform()
    except Exception as e:
        print("exception at move_mouse_to_center")
        print(e)
    return