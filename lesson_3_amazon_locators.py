# Find the most optimal locators for create account on Amazon

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

# Amazon logo locator
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Create account locator
driver.find_element(By.CSS_SELECTOR, "h1")

# Your name box locator
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Email locator
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password locator
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password must be at lest 6 characters locator
driver.find_element(By.CSS_SELECTOR, ".a-box.a-alert-inline-info")

# Re-enter password locator
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Create your account locator
driver.find_element(By.CSS_SELECTOR, "#continue")

# conditions of use locator
driver.find_element(By.CSS_SELECTOR, "[href*='con']")

# Privacy Notice locator
driver.find_element(By.CSS_SELECTOR, '')

#Sign in link locator
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

