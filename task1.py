from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.keys import keys
from selenium.webdriver.chrome.service import service
from selenium.webdriver.support.ui import Webdriverwait
from selenium.webdriver.support import exected_conditions as EC

service = Service("C:/Users/soura/Downloads/chromedriver.exe")
driver = webdriver.chrome(servide=service)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    wait = Webdriverwait(driver, 10)

    username = wait.until(EC.presence_of_element_located(By.NAME, "Username"))
    password = driver.find.element(By.NMAE, "password")

    username.send_keys("Admin")
    password.send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    add_button = wait.until(EC.elemnent_to_be_clickable((By.XPATH, "//button[text()=' Add']")))
    add_button.click()

    PIM_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
    PIM_module.click()

    first_name = wait.untit(EC.element_to_be_clickable((by.XPATH, "//span[text()='PIM']")))
    last_name = driver.find_element(By.NAME, "lastname")


    first_name.send_keys("test")
    last_name.send_keys("Employees")

    login_details_checkbox = driver.find_element (By.XPATH, "//span[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    login_details_checkbox.click()

    username = wait.until(EC.presence_of_element_located((by.XPATH, "//label[text()='username']/../following-siblings::div/input")))
    username.send_keys("testuser123")
    
    password_field = driver.find_element(By.XPATH, "//label[text()='password']/../following-sibling::div/input")
    confirm_password_field = driver.find_element(By.XPATH, "//label[text()='Confirm password']/../following-sibling::div/input")

    password_field.send_keys("password123")
    confirm_password_field.send_keys("differentPass")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    error_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'password do not match')]")))
    print("test Passed -Error Displayed: ", error_msg.text)

except Exception as e :
    print("test failed: ", str(e))

finally:
    time.sleep(5)
    driver.quit()














                                