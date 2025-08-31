from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

username = 'guest'
password = 'welcome2qauto'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(f"https://{username}:{password}@qauto2.forstudy.space")

id_locators = [
    (By.ID, 'aboutSection'),
    (By.ID, 'contactsSection')
]

name_locators = [
    (By.NAME, 'viewport'),
    (By.NAME, 'robots')
]

class_locators = [
    (By.CLASS_NAME, 'btn-primary'),
    (By.CLASS_NAME, 'nav-item'),
    (By.CLASS_NAME, 'alert'),
    (By.CLASS_NAME, 'footer')
]

tag_locators = [
    (By.TAG_NAME, 'button'),
    (By.TAG_NAME, 'a'),
    (By.TAG_NAME, 'div'),
    (By.TAG_NAME, 'h1')
]

link_text_locators = [
    (By.LINK_TEXT, 'ithillel.ua'),
    (By.LINK_TEXT, 'support@ithillel.ua')
]

css_locators = [
    (By.CSS_SELECTOR, "#aboutSection > div > div > div:nth-child(1) > div > p.about-block_descr.lead"),
    (By.CSS_SELECTOR, "#aboutSection > div > div > div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 > div > p.about-block_descr.lead"),
    (By.CSS_SELECTOR, "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(1) > span"),
    (By.CSS_SELECTOR, "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-end.justify-content-md-end.mb-2.mt-3.mt-md-0 > a.contacts_link.display-4"),
    (By.CSS_SELECTOR, "body > app-root > app-global-layout > div > app-footer > footer > div > div > div.col-7.d-flex.flex-column.justify-content-center.footer_item.-left > p:nth-child(2)")
]

xpath_locators = [
    (By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]"),
    (By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]"),
    (By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button"),
    (By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]"),
    (By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]")
]

try:
    for locator_list in [id_locators, name_locators, class_locators, tag_locators, link_text_locators, css_locators, xpath_locators]:
        for by, value in locator_list:
            try:
                element = driver.find_element(by, value)
                print(f'Знайдено елемент: {element.tag_name} за допомогою {by}={value}')
            except:
                print(f'Елемент не знайдено за допомогою {by}={value}')
            time.sleep(0.5)
finally:
    driver.quit()