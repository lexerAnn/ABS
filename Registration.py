import pickle
from selenium import webdriver
import json

url = "http://197.255.85.10/DeviceRegistration"


def load_cookie(drive, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        drive.get(url)
        for cookie in cookies:
            drive.add_cookie(cookie)


driver = webdriver.Chrome(executable_path="D:\webdrive\chromedriver.exe")
load_cookie(driver, "ccookie\cookie.plk")
driver.get(url)



driver.get(url)
