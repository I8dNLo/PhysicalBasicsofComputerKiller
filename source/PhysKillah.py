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
            element = driver.find_element_by_class_name("input-text")
            print("Trying to set login: {}".format(login))
            element.click()
            element.send_keys(login)
        except:
            sleep(1)
            loginf(driver, login, depth+1)
    else:
        exit()


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
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe', chrome_options=options)
except:
    exit()
for login in log_and_pass.keys():
    driver.get(site)
    sleep(1)
    loginf(driver, login, password= log_and_pass.get(login))

    #element = driver.find_element_by_name("login")


#for idx, doc in tqdm_notebook(enumerate(docs)):
    #print('{}. Обработка {}'.format(idx, doc), end=':')
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #try:
    #    driver = webdriver.Chrome('chromedriver/chromedriver.exe', chrome_options=options)
    #except:
    #    pass
    #driver.get(site)
    #element=driver.find_element_by_xpath('//*[@id="module-1-2-1"]/div/input')
    #WebDriverWait(driver, 1)
    #element.send_keys(doc)
    #element.send_keys(Keys.RETURN)



    #class ="input-text" name="login" tabindex="1" id="login-input" >