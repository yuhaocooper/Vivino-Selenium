from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.vivino.com/explore?e=eJwNyTEKgDAMBdDb_Lk5QDbBAziKSKyxFGwraal6e13e8pIxIcXM5BySPEzk4F-eRvifAdf_4eAuFrXJibKxSYs51FW6mgRF4V2rx93mhekDFGYa2A==')

def scroll_down():
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(1)
        element = WebDriverWait(driver,10).until(
            EC.invisibility_of_element((By.CLASS_NAME, 'loader__circle--YmwD1'))
        )
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_down()

#Finding all the elements I want
winery = driver.find_elements_by_css_selector('span.vintageTitle__winery--2YoIr')
winename = driver.find_elements_by_css_selector('span.vintageTitle__wine--U7t9G')
country = driver.find_elements_by_css_selector('div.vintageLocation__vintageLocation--1DF0p')   #.text.split('\n')[0]
region = driver.find_elements_by_css_selector('div.vintageLocation__vintageLocation--1DF0p')    #.text.split('\n')[2]
rating = driver.find_elements_by_css_selector('div.vivinoRatingWide__averageValue--1zL_5')
numberOfRatings = driver.find_elements_by_css_selector('div.vivinoRatingWide__basedOn--s6y0t')
wineHtmlLink = driver.find_elements_by_css_selector('div.cleanWineCard__cleanWineCard--tzKxV.cleanWineCard__row--CBPRR')

list = [winery,winename,country,region,rating,numberOfRatings,wineHtmlLink]
fulllist = []
headers = ['winery','winename','country','region','rating','numberOfRatings','wineHtmlLink']
print(len(winename))
print(len(country))
print(len(region))
print(len(rating))
print(len(numberOfRatings))
print(len(wineHtmlLink))

for i in list:
    if i == country:
        templist = []
        for x in i:
            textname = x.text.split('\n')[0]
            templist.append(textname)
        fulllist.append(templist)
    elif i == region:
        templist = []
        for x in i:
            textname = x.text.split('\n')[2]
            templist.append(textname)
        fulllist.append(templist)
    elif i == numberOfRatings:
        templist = []
        for x in i:
            textname = x.text.split(' ')[0]
            templist.append(textname)
        fulllist.append(templist)
    elif i == wineHtmlLink:
        templist = []
        for x in i:
            linkname = x.find_element_by_css_selector('a').get_attribute('href')
            templist.append(linkname)
        fulllist.append(templist)
    else:
        templist = []
        for x in i:
            textname = x.text
            templist.append(textname)
        fulllist.append(templist)

df = pd.DataFrame({headers[0]:fulllist[0],headers[1]:fulllist[1],headers[2]:fulllist[2],headers[3]:fulllist[3],headers[4]:fulllist[4],headers[5]:fulllist[5]})
df.to_csv('output.csv', mode='a', encoding='utf-8-sig', index=False)

driver.quit()
