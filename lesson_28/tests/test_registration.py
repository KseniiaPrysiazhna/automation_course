import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Registration")
@allure.story("Successful user registration")
def test_user_registration(driver, registration_page, open_registration_form):
    with allure.step("Fill user details"):
        driver.find_element(*registration_page.FIRSTNAME_INPUT).send_keys("Test")
        driver.find_element(*registration_page.LASTNAME_INPUT).send_keys("User")
        driver.find_element(*registration_page.EMAIL_INPUT).send_keys(f"test{int(time.time())}@mail.com")
        driver.find_element(*registration_page.PASSWORD_INPUT).send_keys("Test1234!")
        driver.find_element(*registration_page.REPASSWORD_INPUT).send_keys("Test1234!")

    with allure.step("Click Register button"):
        register_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(registration_page.REGISTER_BUTTON)
        )
        register_btn.click()

    with allure.step("Verify registration success"):
        register_btn = driver.find_element(*registration_page.REGISTER_BUTTON)
        assert not register_btn.is_enabled(), "Registration failed: Register button still enabled"