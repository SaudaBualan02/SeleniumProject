from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login():
    # Initialize the ChromeDriver
    driver = webdriver.Chrome()
    # Open the login page
    driver.get("https://www.facebook.com/")  # Replace with the actual login page URL

    try:
        # Find the username and password input fields and the login button
        username_field = driver.find_element(By.ID, "email")  # Replace "username" with the actual ID of the username field
        password_field = driver.find_element(By.ID, "pass")  # Replace "password" with the actual ID of the password field
        login_button = driver.find_element(By.NAME, "login")  # Replace "login-button" with the actual ID of the login button

        # Enter the username and password
        username_field.send_keys("09850175301")  # Replace with your actual username
        password_field.send_keys("Tayamot02")  # Replace with your actual password

        # Click the login button
        login_button.click()

        # Wait for the page to load after login (you can adjust the waiting time as needed)
        time.sleep(3)

        # Here, we can check if the login is successful by looking for a specific element that only exists on the logged-in page
        # For example, if there is a "logout" link on the logged-in page
        try:
            logout_link = driver.find_element(By.LINK_TEXT,"Log Out")  # Replace "Logout" with the actual text of the logout link
            print("Login successful!")
        except:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()