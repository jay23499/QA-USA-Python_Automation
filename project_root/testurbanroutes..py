import pytest
from selenium import webdriver
from pages.urban_routes_page import UrbanRoutesPage
import data
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if not helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            raise Exception("Cannot connect to Urban Routes server. Check if it is running.")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.page.enter_from(data.ADDRESS_FROM)
        self.page.enter_to(data.ADDRESS_TO)

    def test_select_plan(self):
        self.page.select_plan(data.PLAN_NAME)

    def test_fill_phone_number(self):
        self.page.enter_phone(data.PHONE_NUMBER)

    def test_fill_card(self):
        self.page.enter_card(data.CARD_NUMBER)
        self.page.enter_card_code(data.CARD_CODE)

    def test_comment_for_driver(self):
        self.page.enter_message(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self.page.add_item("Blanket")
        self.page.add_item("Handkerchiefs")

    def test_order_ice_creams(self):
        for _ in range(2):
            self.page.add_item("Ice Cream")

    def test_submit_order(self):
        self.page.submit_order()
        success_text = self.page.get_success_message()
        assert "Order created" in success_text
