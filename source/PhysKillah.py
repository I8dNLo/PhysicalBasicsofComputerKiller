from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

import os
from sys import exit
from time import sleep
def loginf(driver, login, password, depth=0):
    if depth<5:
        try:
            Login_element = driver.find_element_by_name("login")
            Password_element = driver.find_element_by_name("password")

            print("Trying to set login: {}".format(login))
            Login_element.send_keys(login)
            Password_element.send_keys(password)
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

def like_fresh_posts(driver):
    e = driver.find_element_by_css_selector("#nav > ul > li:nth-child(2) > a")
    e.click()
    es = driver.find_elements_by_class_name("plus")
    es_len = len(es)
    for i in range(es_len):
        if i<es_len-1:
            es = driver.find_elements_by_class_name("plus")
            es[i].click()

path= os.path.dirname(__file__)
site = 'http://compblog.ilc.edu.ru/login/'

with open("../accounts/Accounts.txt", "r") as file:
    log_and_pass = dict()
    non_bot_set = set()
    for line in file:
        login, password, is_bot = line.split(" ")
        log_and_pass.update({login:password})
        if "False" in is_bot:
            non_bot_set.update({login})

print(non_bot_set)
options = webdriver.ChromeOptions()
print(path)
options.add_argument('headless')
try:
    driver = webdriver.Chrome('../chromedriver/chromedriver2.exe', chrome_options=options)
except:
    exit()
for login in log_and_pass.keys():
    driver.get(site)
    sleep(1)
    loginf(driver, login, password= log_and_pass.get(login))
    for page in  non_bot_set.difference(set(login)):
        print("Liking {}".format(page))
        add_raiting(driver, page.split("@")[0])
        like_fresh_posts(driver)
driver.close()
