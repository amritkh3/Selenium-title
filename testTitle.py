"""Checking if the title is right while automation testing
1. import time  from python
2. import webdriver from selenium.
3.import chromedrivermanager.in order to import chromedrivermanager 
ask pip to installwebdriver_manager
4.install chromedrivermanager and assign it to the variale driver.
5.use get fumction to open the web page with the help of url.
ie.driver.get("url")
6.user driver.title function to get the title and assign it to variable 
checkTitle.
7.use if condition if the check title is same as it was supposed to be 
   print pass as result
  else print fail result 
"""
import time#this is python time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager#if weddriver_manager is not found run
#pip install webdrive_manager

driver = webdriver.Chrome(ChromeDriverManager().install())# your entire selenium chrome package
driver.get('https://www.google.com')
driver.maximize_window()#maximize the window
# time.sleep(3)#this will hold the time for 3 seconds
checkTitle=driver.title
# print(checkTitle)
if (checkTitle=="Google"):
    print("test case one: passed")
else :
    print("test case one failed")    


time.sleep(3)#this will hold the time for 3 sec
driver.quit()#you need to close the web everytime using this driver.quit()function



  

