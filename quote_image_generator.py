import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random

# initialize driver
driver = webdriver.Chrome() #my webdriver is in path's folder

# The site we are using
driver.get('https://quotescover.com/tools/online-quotes-maker')
driver.implicitly_wait(20)
time.sleep(5)


#List Of Quotes
quotes = [

"Never share your secrets", "EAT SLEEP CODE AND REPEAT", "Success is a state of mind", "Legends Never Die"

]

m = len(quotes)
n = random.randint(0,m-1)

random_quote = quotes[n] #It is a Random Quote From The List

addtext = driver.find_element_by_name("comment")
addtext.click()
addtext.clear()
addtext.send_keys(random_quote)

time.sleep(1)

# We clear the author cuz we dont know the author
add_author = driver.find_element_by_id("inputSecondText")
add_author.clear()

time.sleep(2)

download = driver.find_element_by_class_name("openDownload")
time.sleep(1)
download.click()

# 20 seconds taken by the site, not by the program
time.sleep(20) 

jpg = driver.find_element_by_xpath('//small[text()="(compressed)"]')
jpg.click()

final_download = driver.find_element_by_class_name("save_image_locally_jpg")
final_download.click()