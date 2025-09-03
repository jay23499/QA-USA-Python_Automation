# pages.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


class UrbanRoutesPage:
    def __init__(self, driver, wait_time: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    # ---------- Address ----------
    def fill_address_from(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-from")))
        el.clear()
        el.send_keys(address)

    def fill_address_to(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-to")))
        el.clear()
        el.send_keys(address)

    def get_from(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-from")))
        return el.get_attribute("value")

    def get_to(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-to")))
        return el.get_attribute("value")

    # ---------- Tariff Plan ----------
    def select_supportive_plan(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='tariff-supportive']"))
        )
        if "active" not in btn.get_attribute("class"):
            btn.click()

    def is_plan_selected(self, plan_name: str) -> bool:
        # assumes the active plan button has "active" in class
        if plan_name.lower() == "supportive":
            btn = self.driver.find_element(By.CSS_SELECTOR, "[data-test='tariff-supportive']")
            return "active" in btn.get_attribute("class")
        return False

    # ---------- Phone ----------
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

    def is_phone_verified(self) -> bool:
        return "phone verified" in self.driver.page_source.lower()

    # ---------- Card ----------
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

    def is_card_linked(self) -> bool:
        return "card linked" in self.driver.page_source.lower()

    # ---------- Message ----------
    def add_message_for_driver(self, message: str):
        msg_box = self.wait.until(EC.visibility_of_element_located((By.ID, "comment")))
        msg_box.clear()
        msg_box.send_keys(message)

    def get_entered_message(self) -> str:
        msg_box = self.driver.find_element(By.ID, "comment")
        return msg_box.get_attribute("value")

    # ---------- Items ----------
    def order_blanket_and_handkerchiefs(self):
        blanket_toggle = self.wait.until(EC.element_to_be_clickable((By.ID, "blanket")))
        blanket_toggle.click()
        handkerchiefs_toggle = self.wait.until(EC.element_to_be_clickable((By.ID, "handkerchiefs")))
        handkerchiefs_toggle.click()

    def is_item_selected(self, item_name: str) -> bool:
        try:
            if item_name.lower() == "blanket":
                el = self.driver.find_element(By.ID, "blanket")
            elif item_name.lower() == "handkerchiefs":
                el = self.driver.find_element(By.ID, "handkerchiefs")
            elif item_name.lower() == "ice cream":
                el = self.driver.find_element(By.ID, "icecream")
            else:
                return False
            return "active" in el.get_attribute("class")
        except Exception:
            return False

    def order_icecreams(self, count: int = 2):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "icecream")))
        for _ in range(count):
            btn.click()

    def get_item_count(self, item_name: str) -> int:
        if item_name.lower() == "ice cream":
            els = self.driver.find_elements(By.CSS_SELECTOR, "#icecream.active")
            return len(els)
        return 0

    # ---------- Order ----------
    def order_taxi_and_wait_for_car_search_modal(self) -> bool:
        order_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "order-taxi")))
        order_btn.click()
        modal = self.wait.until(EC.visibility_of_element_located((By.ID, "car-search-modal")))
        return modal.is_displayed()
