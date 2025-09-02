import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def open_registration_form(driver, home_page):
    driver.find_element(*home_page.SIGNUP_BUTTON).click()