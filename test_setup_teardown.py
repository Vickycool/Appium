import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


class Test_ABC:
    # 函数级开始
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '611AFBPJ24FEV'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 函数级结束
    def teardown_class(self):
        self.driver.quit()
        print("------->teardown_class")

    def waitfor(self, xpath):
        return WebDriverWait(self.driver, timeout=5, poll_frequency=0.5).until(lambda x: x.find_element_by_xpath(xpath))

    def test_b(self):
        print(self.driver.find_element_by_xpath("//*[contains(@text,'确定')]"))
        # self.waitfor("//*[contains('@text','确定')]").click()
        # time.sleep(5)
        # self.waitfor("//*[contains('@text','免打扰')]").click()
        # self.driver.close_app()


if __name__ == '__main__':
    pytest.main(['s'],["test_setup_teardown.py"])