from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")