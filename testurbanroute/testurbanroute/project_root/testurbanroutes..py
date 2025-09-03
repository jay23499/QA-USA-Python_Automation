from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Route ---
    def enter_from(self, address):
        from_field = self.wait.until(EC.element_to_be_clickable((By.ID, "from")))
        from_field.clear()
        from_field.send_keys(address)
        from_field.send_keys(Keys.RETURN)

    def enter_to(self, address):
        to_field = self.wait.until(EC.element_to_be_clickable((By.ID, "to")))
        to_field.clear()
        to_field.send_keys(address)
        to_field.send_keys(Keys.RETURN)

    # --- Tariff Plans ---
    def select_plan(self, plan_name):
        plan = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{plan_name}']")))
        plan.click()

    def is_plan_selected(self, plan_name):
        selected = self.driver.find_elements(By.XPATH, f"//div[text()='{plan_name}' and contains(@class, 'active')]")
        return len(selected) > 0

    # --- Phone Number ---
    def enter_phone(self, phone_number):
        phone_field = self.wait.until(EC.element_to_be_clickable((By.ID, "phone")))
        phone_field.clear()
        phone_field.send_keys(phone_number)
        phone_field.send_keys(Keys.RETURN)

    def enter_sms_code(self, code):
        code_field = self.wait.until(EC.element_to_be_clickable((By.ID, "code")))
        code_field.clear()
        code_field.send_keys(code)
        code_field.send_keys(Keys.RETURN)

    def is_phone_verified(self):
        return "verified" in self.driver.page_source.lower()

    # --- Payment Card ---
    def enter_card(self, card_number):
        card_field = self.wait.until(EC.element_to_be_clickable((By.ID, "number")))
        card_field.clear()
        card_field.send_keys(card_number)

    def enter_card_code(self, card_code):
        code_field = self.wait.until(EC.element_to_be_clickable((By.ID, "code")))
        code_field.clear()
        code_field.send_keys(card_code)

    def switch_focus_out(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)

    def confirm_card_linked(self):
        link_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Link']")))
        link_btn.click()

    def is_card_linked(self):
        return "card linked" in self.driver.page_source.lower()

    # --- Message for Driver ---
    def enter_message(self, message):
        msg_field = self.wait.until(EC.element_to_be_clickable((By.ID, "comment")))
        msg_field.clear()
        msg_field.send_keys(message)

    def get_entered_message(self):
        msg_field = self.driver.find_element(By.ID, "comment")
        return msg_field.get_attribute("value")

    # --- Extra Items ---
    def add_item(self, item_name):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item_name}']")))
        btn.click()

    def is_item_selected(self, item_name):
        selected = self.driver.find_elements(By.XPATH, f"//div[text()='{item_name}' and contains(@class, 'active')]")
        return len(selected) > 0

    def get_item_count(self, item_name):
        items = self.driver.find_elements(By.XPATH, f"//div[text()='{item_name}' and contains(@class, 'active')]")
        return len(items)

    # --- Order Submission ---
    def submit_order(self):
        order_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Order')]")))
        order_btn.click()

    def get_modal_message(self):
        modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "order-modal")))
        return modal.text
