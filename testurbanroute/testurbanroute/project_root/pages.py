# pages/urban_routes_page.py
from importlib import import_module

import pages.urban_routes_page
import selenium.webdriver.remote.webdriver

class UrbanRoutesPage:
    def __init__(self, driver: selenium.webdriver.remote.webdriver.WebDriver):
        self.driver = driver

    # Locators
    FROM_INPUT = (By.ID, "address_from")
    TO_INPUT = (By.ID, "address_to")
    PHONE_INPUT = (By.ID, "phone")
    CARD_INPUT = (By.ID, "card")
    CARD_CODE_INPUT = (By.ID, "card_code")
    MESSAGE_INPUT = (By.ID, "message_for_driver")
    PLAN_SELECT = (By.ID, "plan")  # adjust if the plan selection is different
    ITEM_ADD_BUTTON = (By.CLASS_NAME, "add-item")  # example, adjust as needed
    SUBMIT_BUTTON = (By.ID, "submit_order")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")  # adjust according to actual HTML

    # Page methods
    def enter_from(self, address: str):
        elem = self.driver.find_element(*self.FROM_INPUT)
        elem.clear()
        elem.send_keys(address)

    def enter_to(self, address: str):
        elem = self.driver.find_element(*self.TO_INPUT)
        elem.clear()
        elem.send_keys(address)

    def enter_phone(self, phone: str):
        elem = self.driver.find_element(*self.PHONE_INPUT)
        elem.clear()
        elem.send_keys(phone)

    def enter_card(self, card_number: str):
        elem = self.driver.find_element(*self.CARD_INPUT)
        elem.clear()
        elem.send_keys(card_number)

    def enter_card_code(self, card_code: str):
        elem = self.driver.find_element(*self.CARD_CODE_INPUT)
        elem.clear()
        elem.send_keys(card_code)

    def enter_message(self, message: str):
        elem = self.driver.find_element(*self.MESSAGE_INPUT)
        elem.clear()
        elem.send_keys(message)

    def select_plan(self, plan_name: str):
        plan_element = self.driver.find_element(*self.PLAN_SELECT)
        for option in plan_element.find_elements(By.TAG_NAME, "option"):
            if option.text == plan_name:
                option.click()
                break

    def add_item(self, item_name: str):
        # Assumes each item has a button with text matching the item name
        buttons = self.driver.find_elements(*self.ITEM_ADD_BUTTON)
        for btn in buttons:
            if btn.text.strip() == item_name:
                btn.click()
                break

    def submit_order(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_success_message(self) -> str:
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text


def urban_routes_page():
    return None