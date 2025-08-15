import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_set_route(self):
        self.page.set_route("New York", "Boston")

    def test_select_plan(self):
        self.page.select_plan("Premium")

    def test_fill_phone_number(self):
        self.page.fill_phone_number("1234567890")

    def test_fill_card(self):
        self.page.fill_card("4111111111111111", "12/25", "123")

    def test_comment_for_driver(self):
        self.page.comment_for_driver("Please drive safely and play jazz music.")

    def test_order_blanket_and_handkerchiefs(self):
        self.page.order_accessories(["blanket", "handkerchief"])

    def test_car_search_model_appears(self):
        assert self.page.search_car_model("Tesla Model 3")

    def test_order_2_ice_creams(self):
        orders = [
            {"flavor": "Chocolate", "quantity": 1},
            {"flavor": "Strawberry", "quantity": 1}
        ]
        self.page.order_multiple_icecreams(orders)
