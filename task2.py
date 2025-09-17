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
    password = driver.find.element(By.NAME, "password")

    username.send_keys("Admin")
    password.send_keys("password123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    #PIM module
    PIM_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
    PIM_module.click()

    #add new employees
    first_name = wait.untit(EC.element_to_be_clickable((by.XPATH, "//span[text()='PIM']")))
    last_name = driver.find_element(By.NAME, "lastname")

    first_name.send_keys("Sourabh")
    last_name.send_keys("Singh")

    #Now login details for new employees
    login_details_checkbox = driver.find_element (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active label-right']")
    login_details_checkbox.click()

    emp_username = wait.until(EC.presence_of_element_located((by.XPATH, "//label[text()='username']/../following-siblings::div/input")))
    emp_username.send_keys("Sourabh.singh")

    emp_password = driver.find_element(By.XPATH, "//label[text()='password']/../following-sibling::div/input")
    emp_confirm_password = driver.find_element(By.XPATH, "//label[text()='Confirm password']/../following-sibling::div/input")

    emp_password.send_keys("Employee123")
    emp_confirm_password.send_keys("Employee123")

    #saving new Emp details
    driver.find_element(by.XPATH, "//button[@tyoe='submit']").click()
    time.sleep(3)

    #Log out as the admin
    profile_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[#class=oxd-userdropdown-tab]")))
    profile_menu.click()
    logout_btn = wait.until(EC.presense_of_element_to_be_clickable((By.XPATH, "//a[text(='logout')]")))
    logout_btn.click()

    # login
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password - driver.find_element(By.NAME, "password")

    username.send_keys("sourabh.singh")
    password.send_keys("Employees123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    #dashboard verify
    dashboard_text = wait.until(EC.presence_of_element_located((by.XPATH, "//h6[text()='Dashboard']")))
    if dashboard_text.is_displayed():
        print("test passed")
    else:
        print("test Failed")

except Exception as e:
    print("test Failed:", str(e))

finally:
    time.sleep(5)
    driver.quit()
    






