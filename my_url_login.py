from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

username = "123"
password = "321"

url = "https://www.circula.com/de"

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)



# sleep(100)