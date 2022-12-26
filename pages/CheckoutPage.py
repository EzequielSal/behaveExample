import time

from driver_interactions.ElementsInteractions import ElementsWebInteractions


class CheckoutPage(ElementsWebInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_first_name = "first-name"
    id_last_name = "last-name"
    id_zip_postalCode = "postal-code"
    id_press_button_continue = "continue"
    class_title_page_purchase_checkout = "title"
    id_press_button_finish = "finish"
    class_title_TKP = "complete-header"
    id_press_button_backtoproducts = "back-to-products"

    def send_info_checkout(self, name, lastname, zipcode):
        self.send_text(name, self.id_first_name, "id")
        self.send_text(lastname, self.id_last_name, "id")
        self.send_text(zipcode, self.id_zip_postalCode, "id")

    def press_button_continue(self):
        self.press_element(self.id_press_button_continue, "id")
        time.sleep(5)

    def verify_page_purchase_checkout(self):
        title_page_purchase_checkout = self.get_text(self.class_title_page_purchase_checkout, "class")
        if title_page_purchase_checkout != "CHECKOUT: OVERVIEW":
            assert False

    def press_button_purchase(self):
        self.press_element(self.id_press_button_finish, "id")
        time.sleep(5)

    def verify_TKP(self):
        title_TKP = self.get_text(self.class_title_TKP, "class")
        if title_TKP != "THANK YOU FOR YOUR ORDER":
            assert False

    def press_button_back_to_products(self):
        self.press_element(self.id_press_button_backtoproducts, "id")
        time.sleep(5)
