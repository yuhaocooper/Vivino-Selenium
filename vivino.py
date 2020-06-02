"""
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://nba.com")
print(driver.title)
driver.quit()
"""

from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://books.toscrape.com/catalogue/page-3.html")
classname = driver.find_element_by_css_selector('article.product_pod > h3 > a').text

print(classname)

driver.quit()
