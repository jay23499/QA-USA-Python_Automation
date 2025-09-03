import pytest
import data
import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage


class TestUrbanRoutesFullFlow:

    @classmethod
    def setup_class(cls):
        """Set up Chrome driver once per class."""
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def setup_method(self):
        """Open the Urban Routes app before each test."""
        self.driver.get(data.URBAN_ROUTES_URL)
        self.routes_page = UrbanRoutesPage(self.driver)

    # ---------------- Tests ----------------

    def test_set_address(self):
        self.routes_page.fill_address_from(data.ADDRESS_FROM)
        self.routes_page.fill_address_to(data.ADDRESS_TO)
        assert self.routes_page.get_from() == data.ADDRESS_FROM
        assert self.routes_page.get_to() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.routes_page.select_supportive_plan()
        assert self.routes_page.is_plan_selected("Supportive")

    def test_fill_phone_number(self):
        self.routes_page.add_phone_number(data.PHONE_NUMBER)
        assert self.routes_page.is_phone_verified()

    def test_add_card(self):
        self.routes_page.add_card_details(data.CARD_NUMBER, data.CARD_CODE)
        assert self.routes_page.is_card_linked()

    def test_add_message_for_driver(self):
        self.routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.routes_page.get_entered_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.order_blanket_and_handkerchiefs()
        assert self.routes_page.is_item_selected("Blanket")
        assert self.routes_page.is_item_selected("Handkerchiefs")

    def test_order_icecreams(self):
        self.routes_page.order_icecreams(count=2)
        assert self.routes_page.get_item_count("Ice Cream") == 2

    def test_order_taxi_supportive(self):
        self.routes_page.fill_address_from(data.ADDRESS_FROM)
        self.routes_page.fill_address_to(data.ADDRESS_TO)
        self.routes_page.select_supportive_plan()
        self.routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        modal_visible = self.routes_page.order_taxi_and_wait_for_car_search_modal()
        assert modal_visible is True, "Car search modal did not appear"

    # ---------------- Teardown ----------------
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
