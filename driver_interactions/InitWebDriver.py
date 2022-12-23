from selenium import webdriver


class InitWebDriver:

    @staticmethod
    def init_web_driver():
        web_driver = webdriver.Chrome("chromedriver.exe")
        web_driver.maximize_window()
        return web_driver
