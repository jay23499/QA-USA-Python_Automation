# main.py
import pytest
from pages import UrbanRoutesPage
from data import (
    URBAN_ROUTES_URL,
    ADDRESS_FROM,
    ADDRESS_TO,
    PHONE_NUMBER,
    CARD_NUMBER,
    CARD_CODE,
    MESSAGE_FOR_DRIVER,
)
from helpers import create_driver, is_url_reachable

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        """Class-level setup: check URL and initialize driver"""
        if not is_url_reachable(URBAN_ROUTES_URL):
            raise Exception(f"URL {URBAN_ROUTES_URL} is not reachable. Cannot run tests.")

        cls.driver, cls.wait = create_driver()
        cls.driver.get(URBAN_ROUTES_URL)
        cls.driver.maximize_window()
        cls.page = UrbanRoutesPage(cls.driver, cls.wait)

    @classmethod
    def teardown_class(cls):
        """Class-level teardown: quit the driver"""
        cls.driver.quit()

    def test_fill_address_from(self):
        self.page.fill_address_from(ADDRESS_FROM)
        assert self.page.driver.find_element(*UrbanRoutesPage.FROM_FIELD).get_attribute("value") == ADDRESS_FROM

    def test_fill_address_to(self):
        self.page.fill_address_to(ADDRESS_TO)
        assert self.page.driver.find_element(*UrbanRoutesPage.TO_FIELD).get_attribute("value") == ADDRESS_TO

    def test_route_displayed(self):
        self.page.fill_address_from(ADDRESS_FROM)
        self.page.fill_address_to(ADDRESS_TO)
        assert self.page.route_is_displayed()

    def test_fill_phone(self):
        self.page.fill_phone(PHONE_NUMBER)
        assert PHONE_NUMBER in self.page.driver.find_element(*UrbanRoutesPage.PHONE_FIELD).get_attribute("value")

    def test_next_button(self):
        self.page.click_next()
        assert self.page.driver.find_element(*UrbanRoutesPage.CARD_FIELD)

    def test_fill_card_details(self):
