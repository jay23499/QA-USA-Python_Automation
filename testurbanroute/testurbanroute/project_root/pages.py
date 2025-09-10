# pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UrbanRoutesPage:
    """Page Object Model for the Urban Routes App"""

    # --- LOCATORS ---
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    SUGGESTION = (By.CLASS_NAME, "suggestion")
    PHONE_FIELD = (By.ID, "phone")
    NEXT_BUTTON = (By.CLASS_NAME, "button")
    CARD_FIELD = (By.ID, "number")
    CODE_FIELD = (By.ID, "code")
    MESSAGE_FIELD = (By.ID, "comment")
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    ROUTE_INFO = (By.CLASS_NAME, "route-details")
    ORDER_CONFIRMATION = (By.CLASS_NAME, "order-confirm")  # replace with real class/ID

    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    # --- METHODS TO INTERACT WITH ELEMENTS ---
    def fill_address_from(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located(self.FROM_FIELD))
        el.clear()
        el.send_keys(address)
        suggestion = self.wait.until(EC.visibility_of_element_located(self.SUGGESTION))
        suggestion.click()

    def fill_address_to(self, address: str):
        el = self.wait.until(EC.visibility_of_element_located(self.TO_FIELD))
        el.clear()
        el.send_keys(address)
        suggestion = self.wait.until(EC.visibility_of_element_located(self.SUGGESTION))
        suggestion.click()

    def fill_phone(self, phone: str):
        el = self.wait.until(EC.visibility_of_element_located(self.PHONE_FIELD))
        el.clear()
        el.send_keys(phone)

    def click_next(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        btn.click()

    def fill_card_details(self, number: str, code: str):
        card = self.wait.until(EC.visibility_of_element_located(self.CARD_FIELD))
        card.clear()
        card.send_keys(number)
        code_field = self.wait.until(EC.visibility_of_element_located(self.CODE_FIELD))
        code_field.clear()
        code_field.send_keys(code)

    def fill_message(self, message: str):
        el = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_FIELD))
        el.clear()
        el.send_keys(message)

    def click_order(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        btn.click()

    def route_is_displayed(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.ROUTE_INFO)) is not None

    def order_is_confirmed(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.ORDER_CONFIRMATION)) is not None

    # --- Example of loop moved to the page class ---
    def order_multiple_icecreams(self, flavors: list):
        """Loop through a list of icecream flavors and add them to the order"""
        for flavor in flavors:
            flavor_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//button[text()='{flavor}']"))
            )
            flavor_element.click()
