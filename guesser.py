import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




url = 'https://www.nytimes.com/games/wordle/index.html'
#url = 'https://finance.yahoo.com/quote/AAPL/chart?p=AAPL#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjMuMTk3MTgzMDk4NTkxNTQ5NSwiZmxpcHBlZCI6ZmFsc2UsInZvbHVtZVVuZGVybGF5Ijp0cnVlLCJhZGoiOnRydWUsImNyb3NzaGFpciI6dHJ1ZSwiY2hhcnRUeXBlIjoibGluZSIsImV4dGVuZGVkIjpmYWxzZSwibWFya2V0U2Vzc2lvbnMiOnt9LCJhZ2dyZWdhdGlvblR5cGUiOiJvaGxjIiwiY2hhcnRTY2FsZSI6ImxpbmVhciIsInBhbmVscyI6eyJjaGFydCI6eyJwZXJjZW50IjoxLCJkaXNwbGF5IjoiQUFQTCIsImNoYXJ0TmFtZSI6ImNoYXJ0IiwiaW5kZXgiOjAsInlBeGlzIjp7Im5hbWUiOiJjaGFydCIsInBvc2l0aW9uIjpudWxsfSwieWF4aXNMSFMiOltdLCJ5YXhpc1JIUyI6WyJjaGFydCIsIuKAjHZvbCB1bmRy4oCMIl19fSwic2V0U3BhbiI6bnVsbCwibGluZVdpZHRoIjoyLCJzdHJpcGVkQmFja2dyb3VuZCI6dHJ1ZSwiZXZlbnRzIjp0cnVlLCJjb2xvciI6IiMwMDgxZjIiLCJzdHJpcGVkQmFja2dyb3VkIjp0cnVlLCJyYW5nZSI6bnVsbCwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJBQVBMIiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IkFBUEwiLCJxdW90ZVR5cGUiOiJFUVVJVFkiLCJleGNoYW5nZVRpbWVab25lIjoiQW1lcmljYS9OZXdfWW9yayJ9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOiJkYXkiLCJ0aW1lVW5pdCI6bnVsbCwic2V0U3BhbiI6bnVsbH1dLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQiLCJwYW5lbE5hbWUiOiJjaGFydCJ9fX19'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)

#Using chrome webdriver to access website
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) 
driver.get(url)



script = 'text'
#js = 'alert("Hello World")'
#driver.execute_script(js)


#ps = driver.page_source
#xPath = ('//*[@id="fin-chartiq"]/div[12]')
xPath = ('//*[contains(@id="board","letters")]/game-row[1]')
xPath = ('//*[@id="board"]/game-row[1]//div/game-tile[1]//div')
#xPath = ('//*[@id="board"]/game-row[1]//div/game-tile[1]//div')
#//*[@id="game"]/game-modal//div/div/div/game-icon//svg



elem = driver.find_element(by=By.XPATH, value = xPath)
elem.send_keys('hello')
elem.send_keys(Keys.RETURN)
#print(elem.text)
#driver.close()
#data= {'water'}
