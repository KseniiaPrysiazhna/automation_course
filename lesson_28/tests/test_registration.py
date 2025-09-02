import time

def test_user_registration(driver, registration_page, open_registration_form):
    driver.find_element(*registration_page.FIRSTNAME_INPUT).send_keys("Test")
    driver.find_element(*registration_page.LASTNAME_INPUT).send_keys("User")
    driver.find_element(*registration_page.EMAIL_INPUT).send_keys(f"test{int(time.time())}@mail.com")
    driver.find_element(*registration_page.PASSWORD_INPUT).send_keys("Test1234!")
    driver.find_element(*registration_page.REPASSWORD_INPUT).send_keys("Test1234!")

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(*registration_page.REGISTER_BUTTON)
    )