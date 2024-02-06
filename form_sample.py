# Importing necessary libraries and setting up Selenium WebDriver:
# - selenium.webdriver for controlling the browser
# - By for locating elements
# - Select for selecting an option from a dropbox element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Creating a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Navigating to the specified URL with the WebDriver
driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

# Filling out the form
driver.find_element(By.ID, "fullName").send_keys("John Doe") # Typing personal full name
driver.find_element(By.ID, "email").send_keys("johndoe@example.com") # Typing personal e-mail
driver.find_element(By.ID, "phoneNumber").send_keys("1234567890") # Typing personal phone number
Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("Manager") # Selecting 'Manager' as desired position
driver.find_element(By.ID, "location1").click() # Selecting 'Remote' as preferred work location
driver.find_element(By.ID, "experienceYears").send_keys("17") # Typing number of years of experience
driver.find_element(By.ID, "skill1").click() # Checking 'HTML' skill
driver.find_element(By.ID, "skill2").click() # Checking 'CSS' skill

# Submitting the form clicking in the button
driver.find_element(By.ID, "jobApplicationForm").submit()

# Checking the success message and printing it in the console
success_message = driver.find_element(By.ID, "successMessage").text
assert "Submission successful!" in success_message
print(success_message)

# Closing the browser
driver.quit()