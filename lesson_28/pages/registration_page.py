from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Registration complete')]")
