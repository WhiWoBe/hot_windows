from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
# driver.get('https://app.circula.com/users/sign_in?lang=de')
driver.implicitly_wait(14)

driver.get('https://www.google.com/')

username = "123"
password = "321"

ele = driver.find_element(By.CLASS_NAME, "gLFyf")
ele.send_keys("1234")
print(ele)
