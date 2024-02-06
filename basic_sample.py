# Importing the webdriver module from the selenium package
from selenium import webdriver

# Creating a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Navigating to the specified URL with the WebDriver
driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

# Printing the title of the page to the console
print("Title: " + driver.title)


from selenium.webdriver.common.by import By

driver.find_element(By.ID, "fullName")

driver.find_element(By.XPATH, "//button[text()='Submit Application']")

driver.find_element(By.CSS_SELECTOR, "input[type='email']")

# Closing the WebDriver and quitting the browser
driver.quit()