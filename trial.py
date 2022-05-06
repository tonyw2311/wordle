import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url = 'https://www.google.com/'
#Using chrome webdriver to access website
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) 
driver.get(url)


xPath = ('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
elem = driver.find_element(by=By.XPATH, value = xPath)
elem.send_keys('hello')
elem.send_keys(Keys.RETURN)
time.sleep(10)
