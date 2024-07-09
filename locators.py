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

# find by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')

# find by XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
# find attribute only remove input and add * its the same thing
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")
