from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")
time.sleep(2)

driver.switch_to.frame("frame1")

text_field1 = driver.find_element(By.ID, "input1")
text_field1.send_keys("Frame1_Secret")

check_button1 = driver.find_element(By.TAG_NAME, "button")
check_button1.click()

alert = Alert(driver)
print("Frame1 alert:", alert.text)
alert.accept()

driver.switch_to.default_content()
time.sleep(1)

driver.switch_to.frame("frame2")

text_field2 = driver.find_element(By.ID, "input2")
text_field2.send_keys("Frame2_Secret")

check_button2 = driver.find_element(By.TAG_NAME, "button")
check_button2.click()

alert = Alert(driver)
print("Frame2 alert:", alert.text)
alert.accept()

time.sleep(2)
driver.quit()