from tkinter import X
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import guesser_function as g


url = 'https://www.nytimes.com/games/wordle/index.html'

#Using chrome webdriver to access website
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window() 
driver.implicitly_wait(20) 
driver.get(url)

#Sends word input to wordle
word = 'adieu'
xPath = ('/html/body')
elem = driver.find_element(by=By.XPATH, value = xPath)
elem.click()
elem.send_keys(word)
elem.send_keys(Keys.RETURN)

#evaluated_word = [elem.get_attribute("outerHTML") for elem in driver.execute_script("""return document.querySelector('game-app:nth-of-type(1)').shadowRoot.querySelector('game-row').shadowRoot.querySelectorAll('game-tile:nth-of-type(1)[letter]')""")]


forbidden_list = []
near_guess_list = []
exact_list = ['#']*5
near_dict = {}
for i in range(1,5):
    time.sleep(3)

    #nested shadow roots
    script = """return document.querySelector('game-app').shadowRoot.querySelector('game-row:nth-of-type(%s)').shadowRoot.querySelectorAll('game-tile[letter]')""" %str(i)
    evaluated_word = [elem.get_attribute("outerHTML") for elem in driver.execute_script(script)]
    #evaluated word = ['<game-tile letter="h" evaluation="absent" reveal=""></game-tile>', '<game-tile letter="e" evaluation="present" reveal=""></game-tile>', '<game-tile letter="l" evaluation="absent" reveal=""></game-tile>', '<game-tile letter="l" evaluation="absent" reveal=""></game-tile>', '<game-tile letter="o" evaluation="absent" reveal=""></game-tile>']

    word, forbidden_list, near_guess_list,exact_list, near_dict = g.guesser(evaluated_word,forbidden_list,near_guess_list,exact_list, near_dict)

    elem.send_keys(word)
    elem.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()
driver.quit()















#JUNK
#//*[@id="game"]/game-modal//div/div/div/game-icon//svg
#/following-sibling::input[@type="hidden"'
#driver.execute_script("""document.querySelector('game-row[letter=""] option').value="hello" """)
#script = 'text'
#js = 'alert("Hello World")'
#driver.execute_script(js)
#ps = driver.page_source
#xPath = ('//*[@id="fin-chartiq"]/div[12]')

#xPath = ('//*[@id="board"]/game-row')
#xPath = ('/html/body/game-app//game-theme-manager/div/div[1]/div/game-row[1]')
#elem.send_keys('hello')
#elem.send_keys(Keys.RETURN)
#print(elem.text)
#driver.close()
#data= {'water'}
