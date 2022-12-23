import time

from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage


class LoginSteps:

    @given("Que estamos en la pantalla de login")
    def varify_login_page(context):
        context.login_page_object = LoginPage(context.web_driver)
        context.login_page_object.verify_login_page()

    @when("Haya ingresado mi usuario y contraseña y presionado entrar {user} {password}")
    def send_user_password(context, user, password):
        context.login_page_object.send_user_password(user, password)
        context.login_page_object.press_login_button()

    @then("Valida que mi sesion este activa")
    def verify_active_session(context):
        context.product_list_page_object = ProductListPage(context.web_driver)
        context.product_list_page_object.verify_product_list_page()\


    @then("Valida que se muestre el mensaje de error")
    def verify_error_message(context):
        context.login_page_object.verify_error_message()

