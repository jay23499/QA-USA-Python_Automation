# main.py
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers

# ---------------- Constants ----------------
URBAN_ROUTES_URL = "https://cnt-9abf1245-7520-4416-b534-038f9c253140.containerhub.tripleten-services.com"
ADDRESS_FROM = "East 2nd Street, 601"
ADDRESS_TO = "1300 1st St"
PHONE_NUMBER = "+1 123 123 72 12"
CARD_NUMBER = "1234 5678 9100 1234"
CARD_CODE = "1111"
MESSAGE_FOR_DRIVER = "Stop at the juice bar, please"
WAIT_TIME = 50


# ---------------- Page Object ----------------
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


# ---------------- Test Class ----------------
class TestUrbanRoutesFullFlow:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        if not helpers.is_url_reachable(URBAN_ROUTES_URL):
            print(f"WARNING: URL {URBAN_ROUTES_URL} not reachable. Proceeding anyway...")
        cls.driver.get(URBAN_ROUTES_URL)
        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def take_screenshot_on_failure(self, test_name: str):
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print(f"Screenshot saved: {path}")

    def test_full_supportive_flow(self):
        try:
            self.page.fill_address_from(ADDRESS_FROM)
            self.page.fill_address_to(ADDRESS_TO)
            self.page.select_supportive_plan()
            self.page.add_phone_number(PHONE_NUMBER)
            self.page.add_card_details(CARD_NUMBER, CARD_CODE)
            self.page.add_message_for_driver(MESSAGE_FOR_DRIVER)
            self.page.order_blanket_and_handkerchiefs()
            self.page.order_icecreams(count=2)
            assert self.page.order_taxi_and_wait_for_car_search_modal() is True, \
                "Car search modal did not appear after ordering a taxi with Supportive tariff"
        except Exception as e:
            self.take_screenshot_on_failure("test_full_supportive_flow")
            raise e
