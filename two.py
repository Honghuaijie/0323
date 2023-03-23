from selenium import webdriver
import unittest
from time import sleep


class Two(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()


    def test_denglu01(self):
        self.driver.get("http://www.rjcs.site:8888/pams")
        self.driver.find_element_by_name("loginName").send_keys("njkjxn")
        self.driver.find_element_by_name("password").send_keys("student")
        self.driver.find_element_by_xpath("//form[@id='fmedit']/div[4]/button").click()
        self.driver.find_element_by_partial_link_text("资产入库").click()
        sleep(1)

    def test_denglu02(self):
        self.driver.get("http://www.rjcs.site:8888/pams")
        self.driver.find_element_by_id("loginName").send_keys("njkjxn")
        self.driver.find_element_by_id("password").send_keys("student")
        self.driver.find_element_by_css_selector("form#fmedit>div:nth-child(4)>button").click()
        self.driver.find_element_by_link_text("个人信息").click()
    def tearDown(self):
        sleep(1)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
