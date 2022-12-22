from driver_interactions.ElementsInteractions import ElementsWebInteractions

class ProductListPage(ElementsWebInteractions):
    def __init__(self, driver):
        super().__init__(driver)
        self.webdriver = driver

    class_title = "title"

    def verify_product_list_page(self):
        title_text = self.get_text(self.class_title, "class")
        if title_text != "PRODUCTS":
            assert False