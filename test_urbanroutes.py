from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    CARD_NUMBER_INPUT = (By.ID, "card-number")
    EXPIRY_DATE_INPUT = (By.ID, "expiry-date")
    CVV_INPUT = (By.ID, "cvv")
    ORDER_BUTTON = (By.CLASS_NAME, "btn-order")
    CONFIRMATION_MSG = (By.XPATH, "//div[@class='confirmation-message']")
    BLANKET_CHECKBOX = (By.ID, "accessory-blanket")
    HANDKERCHIEF_CHECKBOX = (By.ID, "accessory-handkerchief")
    FLAVOR_SELECT = (By.ID, "flavor-select")
    DRIVER_COMMENT_BOX = (By.ID, "driver-comment")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_card(self, card_number: str, expiry_date: str, cvv: str) -> None:
        self._fill_input(self.CARD_NUMBER_INPUT, card_number)
        self._fill_input(self.EXPIRY_DATE_INPUT, expiry_date)
        self._fill_input(self.CVV_INPUT, cvv)

    def _fill_input(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def select_accessory(self, accessory_name: str, select: bool = True) -> None:
        if accessory_name.lower() == "blanket":
            checkbox = self.wait.until(EC.element_to_be_clickable(self.BLANKET_CHECKBOX))
        elif accessory_name.lower() == "handkerchief":
            checkbox = self.wait.until(EC.element_to_be_clickable(self.HANDKERCHIEF_CHECKBOX))
        else:
            raise ValueError(f"Accessory '{accessory_name}' not recognized.")

        if checkbox.is_selected() != select:
            checkbox.click()

    def select_flavor(self, flavor_value: str) -> None:
        select_elem = self.wait.until(EC.element_to_be_clickable(self.FLAVOR_SELECT))
        select = Select(select_elem)
        select.select_by_value(flavor_value)

    def enter_driver_comment(self, comment: str) -> None:
        comment_box = self.wait.until(EC.visibility_of_element_located(self.DRIVER_COMMENT_BOX))
        comment_box.clear()
        comment_box.send_keys(comment)

    def submit_order(self) -> None:
        order_btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        order_btn.click()

    @property
    def get_confirmation_message(self) -> str:
        msg = self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_MSG))
        return msg.text
