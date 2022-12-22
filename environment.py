import time

from driver_interactions.ElementsInteractions import ElementsWebInteractions
from driver_interactions.InitWebDriver import InitWebDriver


def before_all(context):
    context.prepare_driver = InitWebDriver
    context.web_driver = context.prepare_driver.init_web_driver()
    context.interactions_object = ElementsWebInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com/")


def after_all(context):
    time.sleep(10)
    context.web_driver.quit()


"""def before_feature(context):
    
def before_scenario(context):
    
def before_step(contexto):"""