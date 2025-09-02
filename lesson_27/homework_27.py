from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    def enter_invoice_number(self, invoice_number: str):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="en"]'))
        )
        input_field.clear()
        input_field.send_keys(invoice_number)
        input_field.send_keys(Keys.ENTER)

    def get_status_text(self) -> str:
        status_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="chat"]/header/div[2]/div[2]/div[2]')
            )
        )
        return status_element.text.strip()


class TestNovaPoshtaTracking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_tracking_status(self):
        tracking_number = "20451233289549"
        expected_status = "Отримана"

        page = NovaPoshtaTrackingPage(self.driver)
        page.enter_invoice_number(tracking_number)
        actual_status = page.get_status_text()

        self.assertEqual(expected_status, actual_status, f"Очікувався статус '{expected_status}', але отримано '{actual_status}'")


if __name__ == "__main__":
    unittest.main()