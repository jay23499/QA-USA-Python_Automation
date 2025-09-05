import helpers
import data

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        print("function created for set route")
        # TODO: implement route selection

    def test_select_plan(self):
        print("function created for select plan")
        # TODO: implement plan selection

    def test_fill_phone_number(self):
        print("function created for fill phone number")
        # TODO: fill phone number field

    def test_fill_card(self):
        print("function created for fill card")
        # TODO: fill payment info

    def test_comment_for_driver(self):
        print("function created for comment for driver")
        # TODO: add comment for driver

    def test_order_blanket_and_handkerchiefs(self):
        print("function created for order blanket and handkerchiefs")
        # TODO: add items to order

    def test_car_search_model_appears(self):
        print("function created for car search model appears")
        # TODO: check car model appears

    def test_order_2_ice_creams(self):
        print("Function created for order 2 ice creams")
        for i in range(2):
            print(f"Ordering ice cream #{i+1}")
            # TODO: implement ice cream order
