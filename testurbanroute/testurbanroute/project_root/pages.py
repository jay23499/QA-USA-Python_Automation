# pages.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


class UrbanRoutesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def fill_address_from(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-from")))
        el.clear()
        el.send_keys(address)

    def fill_address_to(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-to")))
        el.clear()
        el.send_keys(address)

    def select_supportive_plan(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='tariff-supportive']"))
        )
        if "active" not in btn.get_attribute("class"):
            btn.click()

    def add_phone_number(self, phone_number: str):
        phone_input = self.wait.until(EC.visibility_of_element_located((By.ID, "phone")))
        phone_input.clear()
        phone_input.send_keys(phone_number)

        confirm_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "confirm-phone"))
        )
        confirm_btn.click()

        sms_code_raw = helpers.retrieve_phone_code(phone_number)
        sms_code = str(sms_code_raw) if sms_code_raw else ""
        sms_input = self.wait.until(EC.visibility_of_element_located((By.ID, "sms-code")))
        sms_input.send_keys(sms_code)

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

    def add_message_for_driver(self, message: str):
        msg_box = self.wait.until(EC.visibility_of_element_located((By.ID, "comment")))
        msg_box.clear()
        msg_box.send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        toggle = self.wait.until(EC.element_to_be_clickable((By.ID, "blanket")))
        toggle.click()
        assert "active" in toggle.get_attribute("class")

    def order_icecreams(self, count: int = 2):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "icecream")))
        for _ in range(count):
            btn.click()

    def order_taxi_and_wait_for_car_search_modal(self) -> bool:
        order_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "order-taxi")))
        order_btn.click()
        modal = self.wait.until(EC.visibility_of_element_located((By.ID, "car-search-modal")))
        return modal.is_displayed()
