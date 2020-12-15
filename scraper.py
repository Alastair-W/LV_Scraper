# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd

# specify the url
urlpage = 'https://us.louisvuitton.com/eng-us/products/pochette-accessoires-monogram-005656'
print(urlpage)

# run firefox webdriver from executable path of your choice
opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)

# get web page
driver.get(urlpage)

# sleep for 10s
time.sleep(5)

# find elements by xpath
results = driver.find_elements_by_xpath('//*[@id="__layout"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/button')
# results = driver.find_element_by_class_name('lv-product-stock-indicator')
other_results = driver.find_elements_by_xpath('//*[@id="__layout"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/span')
# text = results.getText()

# print results
print(f'Number of results for "button" is {len(results)}')
print(f'Number of results for "span" is {len(other_results)}')



driver.quit()


# <span class="lv-stock-indicator lv-product-stock-indicator lv-product__stock list-label-m -not-available" style="">
#     Out of stock
#   </span>