# main.py

import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutesFullFlow:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # ---------------- Tests ----------------

    def test_set_address(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_address_from(data.ADDRESS_FROM)
        routes_page.fill_address_to(data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_supportive_plan()
        assert routes_page.is_plan_selected("Supportive")

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_phone_number(data.PHONE_NUMBER)
        assert routes_page.is_phone_verified()

    def test_add_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_card_details(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.is_card_linked()

    def test_add_message_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_entered_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.is_item_selected("Blanket")
        assert routes_page.is_item_selected("Handkerchiefs")

    def test_order_icecreams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_icecreams(count=2)
        assert routes_page.get_item_count("Ice Cream") == 2

    def test_order_taxi_supportive(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_address_from(data.ADDRESS_FROM)
        routes_page.fill_address_to(data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        modal_visible = routes_page.order_taxi_and_wait_for_car_search_modal()
        assert modal_visible is True, "Car search modal did not appear"

    # ---------------- Teardown ----------------
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
