import time

from driver_interactions.ElementsInteractions import ElementsWebInteractions


class ProductListPage(ElementsWebInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    class_title = "title"
    id_product_in_list = "add-to-cart-sauce-labs-backpack"
    class_cart_button = "shopping_cart_link"

    def verify_product_list_page(self):
        title_text = self.get_text(self.class_title, "class")
        if title_text != "PRODUCTS":
            assert False

    def press_add_product_in_list(self):
        self.press_element(self.id_product_in_list, "id")

    def press_cart_button(self):
        self.press_element(self.class_cart_button, "class")
        time.sleep(5)