from driver_interactions.ElementsInteractions import ElementsWebInteractions


class CartPage(ElementsWebInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    class_title_page = "title"
    id_checkout_button = "checkout"

    def verify_cart_page(self):
        if self.get_text(self.class_title_page, "class") != "YOUR CART":
            assert False

    def press_checkout_button(self):
        self.press_element(self.id_checkout_button, "id")