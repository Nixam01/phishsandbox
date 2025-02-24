#https://www.geeksforgeeks.org/selenium-python-tutorial/ -- good tutorial on using selenium within python
#https://www.geeksforgeeks.org/browser-automation-using-selenium/?ref=lbp - example of leveraging selenium for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#line below opens chrome card and gets the particular domain (could be passed as argument)
driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get("https://facebook.com")

time.sleep(2.5)

#examples of interaction with web elements using selenium

#driver.get_screenshot_as_file("filename.png")

# get current url
print(driver.current_url)


#finding element methods
result = len(driver.find_elements(By.TAG_NAME, "meta"))
print(result)

result2 = len(driver.find_elements(By.XPATH, "//input[@type='passwor']"))
print(result2)
driver.quit()