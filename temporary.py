from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://automationexercise.com/")
driver.maximize_window()

# Test Case 1: Register User
driver.find_element(By.XPATH, "//a[@href='/login']").click()
new_user_message = driver.find_element(By.CLASS_NAME, "signup-form").text
assert 'New User Signup!' in new_user_message

driver.close()