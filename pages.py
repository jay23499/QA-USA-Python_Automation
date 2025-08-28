# pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers

class UrbanRoutesPage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    # ---------------- Address ----------------
    def set_route(self, address_from, address_to):
        self.fill_address_from(address_from)
        self.fill_address_to(address_to)

    def fill_address_from(self, address):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-from")))
        el.clear()
        el.send_keys(address)

    def fill_address_to(self, address):
        el = self.wait.until(EC.visibility_of_element_located((By.ID, "address-to")))
        el.clear()
        el.send_keys(address)

    def get_from(self):
        return self.driver.find_element(By.ID, "address-from").get_attribute("value")

    def get_to(self):
        return self.driver.find_element(By.ID, "address-to").get_attribute("value")

    # ---------------- Plan ----------------
    def select_supportive_plan(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='tariff-supportive']"))
        )
        if "active" not in btn.get_attribute("class"):
            btn.click()

    def is_supportive_plan_selected(self):
        btn = self.driver.find_element(By.CSS_SELECTOR, "[data-test='tariff-supportive']")
        return "active" in btn.get_attribute("class")

    # ---------------- Phone ----------------
    def add_phone_number(self, phone_number):
        phone_input = self.wait.until(EC.visibility_of_element_located((By.ID, "phone")))
        phone_input.clear()
        phone_input.send_keys(phone_number)

        confirm_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "confirm-phone")))
        confirm_btn.click()

        sms_code_raw = helpers.retrieve_phone_code(phone_number)
        sms_code = str(sms_code_raw) if sms_code_raw else ""
        sms_input = self.wait.until(EC.visibility_of_element_located((By.ID, "sms-code")))
        sms_input.send_keys(sms_code)

    def get_phone_number(self):
        return self.driver.find_element(By.ID, "phone").get_attribute("value")

    # ---------------- Card ----------------
    def add_card_details(self, card_number, card_code):
        card_input = self.wait.until(EC.visibility_of_element_located((By.ID, "number")))
        card_input.clear()
        card_input.send_keys(card_number)

        code_input = self.wait.until(EC.visibility_of_element_located((By.ID, "code")))
        code_input.clear()
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

        link_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "link-card")))
        link_btn.click()

    def is_card_linked(self):
        link_btn = self.driver.find_element(By.ID, "link-card")
        return "active" in link_btn.get_attribute("class")

    # ---------------- Driver Message ----------------
    def add_message_for_driver(self, message):
        msg_box = self.wait.until(EC.visibility_of_element_located((By.ID, "comment")))
        msg_box.clear()
        msg_box.send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(By.ID, "comment").get_attribute("value")

    # ---------------- Blanket & Handkerchiefs ----------------
    def order_blanket_and_handkerchiefs(self):
        toggle = self.wait.until(EC.element_to_be_clickable((By.ID, "blanket")))
        toggle.click()

    def is_blanket_ordered(self):
        toggle = self.driver.find_element(By.ID, "blanket")
        return "active" in toggle.get_attribute("class")

    # ---------------- Ice Creams ----------------
    def order_icecreams(self, count=2):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "icecream")))
        for _ in range(count):
            btn.click()

    def get_icecream_count(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "#icecream.active"))

    # ---------------- Taxi ----------------
    def order_taxi_and_wait_for_car_search_modal(self):
        order_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "order-taxi")))
        order_btn.click()
        modal = self.wait.until(EC.visibility_of_element_located((By.ID,_
