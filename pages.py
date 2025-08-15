import selenium.webdriver.common.by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    FROM_INPUT = (selenium.webdriver.common.by.By.ID, "from")
    TO_INPUT = (selenium.webdriver.common.by.By.ID, "to")
    PLAN_DROPDOWN = (selenium.webdriver.common.by.By.ID, "plan-select")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def set_route(self, from_city, to_city):
        from_input = self.wait.until(EC.visibility_of_element_located(self.FROM_INPUT))
        from_input.clear()
        from_input.send_keys(from_city)

        to_input = self.wait.until(EC.visibility_of_element_located(self.TO_INPUT))
        to_input.clear()
        to_input.send_keys(to_city)

    def select_plan(self, plan_value):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.PLAN_DROPDOWN))
        from selenium.webdriver.support.ui import Select
        Select(dropdown).select_by_value(plan_value)
