import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('http://www.google.com/')
driver.find_element(By.ID, "W0wltc").click()

search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys('ChromeDriver')

# search_box = driver.find_element('q')
time.sleep(5)

driver.quit()