import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 30)


time.sleep(10)
email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
password_input = wait.until(EC.presence_of_element_located((By.ID, "pass")))
email_input.send_keys("09850175301")
password_input.send_keys( "Tayamot02")

login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()


try:
    print("Login successfully!")
except:
    print("LogIn Failed!")


time.sleep(30)
driver.quit()
#initial commit
#second commit
git add -u
