from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# find by CSS, using id:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

# find by using classes:
driver.find_element(By.CSS_SELECTOR,".nav-input")

# find by attribute
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")

# tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='search Amazon'][type='text']")

# tag + #id , .class + [attributes]   on google chrome

# attributes partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")


