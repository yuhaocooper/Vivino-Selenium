from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import pandas as pd
import numpy as np

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.vivino.com/explore?e=eJzLLbI1VMvNzLO1MFDLTaywNTMwUEuutA12V0sGEi5qBUDp9DTbssSizNSSxBy1_CTbosSSzLz04vjEstSixPRUtXzblNTiZLXykuhYW2MIZQKhzCGUkQkApCYhmA==')

def scroll_down():
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        time.sleep(2)
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(driver,15).until(
            EC.invisibility_of_element((By.CLASS_NAME, 'loader__circle--YmwD1'))
        )
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_down()

cards = driver.find_elements_by_css_selector('div.explorerCard__explorerCard--3Q7_0.explorerPageResults__explorerCard--3q6Qe')
fulllist = []
count = 0
startTime = datetime.now()
print(datetime.now() - startTime)

for x in cards:
    try:
        winery = x.find_element_by_css_selector('span.vintageTitle__winery--2YoIr').text
    except:
        winery = ''
    winename = x.find_element_by_css_selector('span.vintageTitle__wine--U7t9G').text
    country = x.find_element_by_css_selector('div.vintageLocation__vintageLocation--1DF0p').text.split('\n')[0]
    try:
        region = x.find_element_by_css_selector('div.vintageLocation__vintageLocation--1DF0p').text.split('\n')[2]
    except:
        region = ''
    rating = x.find_element_by_css_selector('div.vivinoRatingWide__averageValue--1zL_5').text
    numberOfRatings = x.find_element_by_css_selector('div.vivinoRatingWide__basedOn--s6y0t').text.split(' ')[0]
    wineHtmlLink = x.find_element_by_css_selector('div.cleanWineCard__cleanWineCard--tzKxV.cleanWineCard__row--CBPRR').find_element_by_css_selector('a').get_attribute('href')
    fulllist.append([winery,winename,country,region,rating,numberOfRatings,wineHtmlLink])

    #track progress
    count += 1
    print(count)
    print(winery)
    print(datetime.now() - startTime)

headers = ['winery','winename','country','region','rating','numberOfRatings','wineHtmlLink']
df = pd.DataFrame(data=fulllist,columns=headers)
df.to_csv('cardoutput.csv', mode='a', encoding='utf-8-sig', index=False)

driver.quit()
