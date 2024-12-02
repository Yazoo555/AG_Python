from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Set Firefox options (you can leave binary_location out)
options = Options()

# Specify the path to geckodriver using the Service class
geckodriver_service = Service("/snap/bin/geckodriver")

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=geckodriver_service, options=options)

# Open login page
driver.get("https://admin.ambition.guru/login")  # Replace with actual login URL

# Wait for the user to scan the QR code and authenticate
print("Please scan the QR code and authenticate on the website.")
time.sleep(45)  # Adjust sleep time as needed for the QR code authentication

# Extract cookies after login
cookies = driver.get_cookies()
token = None

# Look for the auth token in the cookies (you can find the correct cookie name by inspecting in DevTools)
for cookie in cookies:
    if 'auth_token' in cookie['name']:  # Replace with the correct name if needed
        token = cookie['value']
        break

if token:
    print(f"Bearer Token: {token}")
else:
    print("Bearer token not found.")