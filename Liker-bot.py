#This is a python-selenium instagram bot which likes the first posts of your instagram feed (usually the first 5)
#Created by antomavr9 ("https://github.com/antomavr9") @ 7/8/2022

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" #Downloade the chromedriver for your Chrome Browser
driver = webdriver.Chrome(PATH)

#----------------------Start------------------------#
driver.get("https://www.instagram.com/accounts/login")
print(driver.title) #prints the title of the website

#---------------Notification Window----------------------#
time.sleep(2)
notifier = driver.find_element("class name", "HoLwm")
notifier.click()
time.sleep(2)

#--------------------Login--------------------------#
loginBar = driver.find_element("name",'username')
loginBar.send_keys("************") #put the username of your instagram account 
loginBar = driver.find_element("name", 'password')
loginBar.send_keys("************") #put the password of your instagram account
loginBar.send_keys(Keys.ENTER)
time.sleep(5)

#---------------Notification Window----------------------#
notifier = driver.find_element("class name", "yWX7d")
notifier.click()
time.sleep(2)

#---------------Notification Window----------------------#
notifier = driver.find_element("class name", "_a9_1")
notifier.click()
time.sleep(2)
print("Notifications Over!")

#--------------Scroll Down and Refresh-------------------#
for i in range(1,3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
    time.sleep(2)    
refresh = driver.find_element("tag name",'body')
refresh.send_keys(Keys.HOME)
time.sleep(2)
print("Refreshed!")

#------------------Like-----------------------------------#
liker = driver.find_elements("class name", "_aamw")
# liker.click()
# print("1 Like!")
print(len(liker))    
for i in range(0,len(liker)):  
    liker[i].click()
    time.sleep(1)
    i=i+1
print("Fin")

#driver.close() #Closes current tab
driver.quit()  #Closes browser