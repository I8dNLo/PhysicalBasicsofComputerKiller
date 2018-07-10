from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import os
from sys import exit
from time import sleep
def loginf(driver, login, password, depth=0):
    if depth<5:
        try:
            Login_element = driver.find_element_by_name("login")
            Password_element = driver.find_element_by_name("password")
            Remember_element = driver.find_element_by_name("remember")

            if Login_element is not None and Password_element is not None:
                print("Login and Password boxes located")
            print("Trying to set login: {}".format(login))
            sleep(0.5)
            Login_element.send_keys(login)
            Password_element.send_keys(password)
            sleep(0.5)
            #Remember_element.click()
            Submit_element = driver.find_element_by_class_name("button")
            Submit_element.click()
            return True
        except NoSuchElementException:
            sleep(1)
            loginf(driver, login, password, depth+1)
    else:
        print("Oooops!")
        exit()

def add_raiting(driver, page):
    driver.get("http://compblog.ilc.edu.ru/profile/" + page)
    Plus_element = driver.find_element_by_class_name("plus")
    Plus_element.click()


path= os.path.dirname(__file__)
site = 'http://compblog.ilc.edu.ru/login/'

with open("../accounts/Accounts.txt", "r") as file:
    log_and_pass = dict()
    for line in file:
        login, password = line.split(" ")
        log_and_pass.update({login:password})

options = webdriver.ChromeOptions()
print(path)
#options.add_argument('headless')
try:
    driver = webdriver.Chrome('../chromedriver/chromedriver2.exe', chrome_options=options)
except:
    exit()
for login in log_and_pass.keys():
    driver.get(site)
    sleep(1)
    loginf(driver, login, password= log_and_pass.get(login))
    for page in  set(log_and_pass.keys()).difference(set(login)):
        print(page)
        add_raiting(driver, page.split("@")[0])
