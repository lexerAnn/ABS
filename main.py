import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

url = "http://197.255.85.10/"
driver.get(url)
path = "ccookie\cookie.plk"

print(driver.title)

inputElementUserName = driver.find_element_by_xpath("//*[@id='UserName']")
inputElementUserName.send_keys('admin')
inputElementPassword = driver.find_element_by_xpath("//*[@id='Password']")
inputElementPassword.send_keys('!intern02')

driver.find_element_by_xpath("//*[@id='body']/section/div/form/fieldset/input").click()


def save_cookie(drive, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(drive.get_cookies(), filehandler)




save_cookie(driver, path)

print(driver.page_source)

print("Finished!")




