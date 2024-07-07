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

driver.get('https://www.target.com/')

# find sign in field and click sign in button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

# click sign in from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(7)

# Verify
expected_text = 'Sign into your Target Account'
actual_text = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
print(actual_text)
print('Test passed')