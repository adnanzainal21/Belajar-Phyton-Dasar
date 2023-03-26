from optparse import Option
from webbrowser import Chrome
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

main_link = 'https://shopee.co.id/xiaomi.official.id#product_list'
path = 'E:\Download\chromedriver_win32'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')

driver = webdriver.Chrome(executable_path = path, options = chrome_options)
driver.get(main_link)

html = driver.excute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html,"html.parser")

product_name = soup.find_all('div',class_='_3Gla5X _2j2K92 _3j20V6')
product_name[0].get_text()


