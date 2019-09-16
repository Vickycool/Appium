from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_elemet(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element(*loc))

    def click(self,loc):
        self.find_elemet(loc).click()

