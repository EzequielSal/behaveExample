from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage


class PurchaseSteps:

    @given("Compra de productos -> Que estamos en la pantalla de login")
    def varify_login_page(context):
        context.login_page_object = LoginPage(context.web_driver)
        context.login_page_object.verify_login_page()

    @when("Compra de productos -> Haya ingresado mi usuario y contraseña y presionado entrar {user} {password}")
    def send_user_password(context, user, password):
        context.login_page_object.send_user_password(user, password)
        context.login_page_object.press_login_button()

    @when("Compra de productos -> Agreguemos un producto al carrito")
    def add_product_cart(context):
        context.product_list_page_object = ProductListPage(context.web_driver)
        context.product_list_page_object.verify_product_list_page()
        context.product_list_page_object.press_add_product_in_list()

    @then("Compra de productos -> Vamos a carrito y continuamos con la compra")
    def press_checkout_button(context):
        context.product_list_page_object.press_cart_button()
        context.cart_page_object = CartPage(context.web_driver)
        context.cart_page_object.verify_cart_page()
        context.cart_page_object.press_checkout_button()