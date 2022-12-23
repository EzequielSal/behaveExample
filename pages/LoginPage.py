from driver_interactions.ElementsInteractions import ElementsWebInteractions


class LoginPage(ElementsWebInteractions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_input_user_text = "user-name"
    id_input_password_text = "password"
    id_login_button = "login-button"
    xpath_error_message = "//div[@class='error-message-container error']"

    def verify_login_page(self):
        if not self.is_element_displayed(self.id_input_user_text, "id"):
            self.log.info("No se encuentra en la pagina de inicio de sesion")
            assert False

    def send_user_password(self, user, password):
        self.send_text(user, self.id_input_user_text, "id")
        self.send_text(password, self.id_input_password_text, "id")

    def press_login_button(self):
        self.press_element(self.id_login_button, "id")

    def verify_error_message(self):
        if not self.is_element_displayed(self.xpath_error_message, "xpath"):
            self.log.info("No se encuentra el mensaje de error")
            assert False



