from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_located(browser):
    print('User language: {}'.format(browser.__user_language))
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector("#add_to_basket_form button.btn-add-to-basket")
