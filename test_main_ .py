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

    # ---------------- Test 1 ----------------
    def test_supportive_flow_addresses_only(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    # ---------------- Test 2 ----------------
    def test_supportive_flow_plan_selection(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_supportive_plan()
        assert routes_page.is_supportive_plan_selected()

    # ---------------- Test 3 ----------------
    def test_add_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_phone_number(data.PHONE_NUMBER)
        assert routes_page.get_phone_number() == data.PHONE_NUMBER

    # ---------------- Test 4 ----------------
    def test_add_card_details(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_card_details(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.is_card_linked()

    # ---------------- Test 5 ----------------
    def test_driver_message(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER

    # ---------------- Test 6 ----------------
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.is_blanket_ordered()

    # ---------------- Test 7 ----------------
    def test_order_icecreams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_icecreams(count=2)
        assert routes_page.get_icecream_count() == 2

    # ---------------- Test 8 ----------------
    def test_order_taxi_and_wait_modal(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.order_taxi_and_wait_for_car_search_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
