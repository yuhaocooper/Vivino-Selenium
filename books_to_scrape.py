#Boilerplate
from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('http://books.toscrape.com/') #the URL of the website we're scraping

filename = "book_titles.txt"  # To save store data

#Getting all the titles in each page
def titlextraction():
    titles = driver.find_elements_by_css_selector('article.product_pod > h3 > a') #Finds all the elements by the css_selector
    with open(filename, 'a+') as f: # a+ option to append file so that the new data is written at the end of file
        for i in titles:
            title = i.get_attribute("title")
            f.write(title + "\n") #'\n' is to create a new line for the next line of data to be added

#loop through all the pages
nextPageElement = driver.find_elements(By.LINK_TEXT,'next')
while(True):
    titlextraction()
    try:
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,'next'))).click() #Asks the driver to wait till the element is clickable, and if its not within 5 seconds, raise a timeout exception
    except TimeoutException: #Handle TimeoutException by closing the driver and stopping the script
        print('No more pages available')
        driver.quit()
        break;
