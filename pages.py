# test_urban_routes_full_flow.py
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers

# ---------------- Constants ----------------
URBAN_ROUTES_URL = "https://cnt-97c9607c-6b24-461f-902c-896ba90ad71f.containerhub.tripleten-services.com"
ADDRESS_FROM = "East 2nd Street, 601"
ADDRESS_TO = "1300 1st St"
PHONE_NUMBER = "+1 123 123 72 12"
CARD_NUMBER = "1234 5678 9100 1234"
CARD_CODE = "1111"
MESSAGE_FOR_DRIVER = "Stop at the juice bar, please"
WAIT_TIME = 50  # Increased wait time for dynamic page


# ---------------- Page Object ----------------
class UrbanRoutesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def switch_to_iframe_if_present(self, iframe_selector: str = None):
        if iframe_selector:
            try:
                iframe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector)))
                self.driver.switch_to.frame(iframe)
            except TimeoutException:
                pass

    def fill_address_from(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-from")))
        el.clear()
        el.send_keys(address)
        self.driver.switch_to.default_content()

    def fill_address_to(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-to")))
        el.clear()
        el.send_keys(address)
        self.driver.switch_to.default_content()

    def select_supportive_plan(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='tariff-supportive']")))
        if "active" not in btn.get_attribute("class"):
            btn.click()
        self.driver.switch_to.default_content()

    def add_phone_number(self, phone_number: str):
        phone_input = self.wait.until(EC.visibility_of_element_located((By.ID, "phone")))
        phone_input.clear()
        phone_input.send_keys(phone_number)

        confirm_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "confirm-phone")))
        confirm_btn.click()

        sms_code_raw = helpers.retrieve_phone_code(phone_number)
        assert sms_code_raw is not None, "SMS code was not retrieved"
        sms_code = str(sms_code_raw)

        sms_input = self.wait.until(EC.visibility_of_element_located((By.ID, "sms-code")))
        sms_input.send_keys(sms_code)
        self.driver.switch_to.default_content()

    def add_card_details(self, card_number: str, card_code: str):
        card_input = self.wait.until(EC.visibility_of_element_located((By.ID, "number")))
        card_input.clear()
        card_input.send_keys(card_number)

        code_input = self.wait.until(EC.visibility_of_element_located((By.ID, "code")))
        code_input.clear()
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

        link_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "link-card")))
        link_btn.click()
        self.driver.switch_to.default_content()

    def add_message_for_driver(self, message: str):
        msg_box = self.wait.until(EC.visibility_of_element_located((By.ID, "comment")))
        msg_box.clear()
        msg_box.send_keys(message)
        self.driver.switch_to.default_content()

    def order_blanket_and_handkerchiefs(self):
        toggle = self.wait.until(EC.element_to_be_clickable((By.ID, "blanket")))
        toggle.click()
        assert "active" in toggle.get_attribute("class")
        self.driver.switch_to.default_content()

    def order_icecreams(self, count: int = 2):

