from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # --- Locators ---
    FROM_CITY_INPUT = (By.ID, "from-city")
    TO_CITY_INPUT = (By.ID, "to-city")
    PLAN_DROPDOWN = (By.ID, "plan-select")
    PHONE_INPUT = (By.ID, "phone")
    CARD_NUMBER_INPUT = (By.ID, "card-number")
    EXPIRY_DATE_INPUT = (By.ID, "expiry-date")
    CVV_INPUT = (By.ID, "cvv")
    DRIVER_COMMENT_BOX = (By.ID, "driver-comment")
    CAR_SEARCH_BOX = (By.ID, "car-search")
    FLAVOR_SELECT = (By.ID, "flavor-select")
    QUANTITY_INPUT = (By.NAME, "quantity")
    ORDER_BUTTON = (By.CLASS_NAME, "btn-order")
    BLANKET_CHECKBOX = (By.ID, "accessory-blanket")
    HANDKERCHIEF_CHECKBOX = (By.ID, "accessory-handkerchief")
    CONFIRMATION_MSG = (By.XPATH, "//div[@class='confirmation-message']")

    # --- Methods ---

    def set_route(self, from_city, to_city):
        self.driver.find_element(*self.FROM_CITY_INPUT).send_keys(from_city)
        self.driver.find_element(*self.TO_CITY_INPUT).send_keys(to_city)

    def select_plan(self, plan_name):
        self.driver.find_element(*self.PLAN_DROPDOWN).send_keys(plan_name)

    def fill_phone_number(self, number):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(number)

    def fill_card(self, card_number, expiry, cvv):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.EXPIRY_DATE_INPUT).send_keys(expiry)
        self.driver.find_element(*self.CVV_INPUT).send_keys(cvv)

    def comment_for_driver(self, comment):
        self.driver.find_element(*self.DRIVER_COMMENT_BOX).send_keys(comment)

    def order_accessories(self, items):
        for item in items:
            if item == "blanket":
                self.driver.find_element(*self.BLANKET_CHECKBOX).click()
            elif item == "handkerchief":
                self.driver.find_element(*self.HANDKERCHIEF_CHECKBOX).click()

    def search_car_model(self, model):
        self.driver.find_element(*self.CAR_SEARCH_BOX).send_keys(model)
        return model in self.driver.page_source  # Replace with better check if available

    def select_flavor(self, flavor):
        self.driver.find_element(*self.FLAVOR_SELECT).send_keys(flavor)

    def set_quantity(self, quantity):
        qty_input = self.driver.find_element(*self.QUANTITY_INPUT)
        qty_input.clear()
        qty_input.send_keys(str(quantity))

    def click_order(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def order_multiple_icecreams(self, orders):
        for order in orders:
            self.select_flavor(order['flavor'])
            self.set_quantity(order['quantity'])
            self.click_order()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.CONFIRMATION_MSG).text
