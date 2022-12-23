from driver_interactions.ElementsInteractions import ElementsWebInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import utilities.Logger as Log
import time

log = Log.func_logger()


def before_all(context):
    log.info("Script iniciado")


def before_scenario(context, scenario):
    context.init_driver_object = InitWebDriver()
    context.web_driver = context.init_driver_object.init_web_driver()
    context.interactions_object = ElementsWebInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com")


def after_scenario(context, scenario):
    context.web_driver.quit()


def after_all(context):
    log.info("Script finalizado")
    time.sleep(5)


"""def before_feature(context):
def before_scenario(context):

def before_step(context):"""