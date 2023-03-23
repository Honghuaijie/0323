from selenium import webdriver
import unittest
from csvv import readData
from ddt import ddt,data,unpack
from selenium.webdriver.support.select import Select
@ddt
class Test(unittest.TestCase):
    @data(*readData())
    @unpack
    def test01(self,name,remark,result):
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.rjcs.site:8888/pams")
        self.driver.find_element_by_id("loginName").send_keys("njkjxn")
        self.driver.find_element_by_name("password").send_keys("student")
        self.driver.find_element_by_tag_name("button").click()
        self.driver.find_element_by_partial_link_text("存放地点").click()
        self.driver.find_element_by_xpath('//*[@id="fmsearch"]/div/button').click()
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(name)
        select=self.driver.find_element_by_xpath('//*[@id="assetTypeId"]')
        Select(select).select_by_value("3")
        self.driver.find_element_by_xpath('//*[@id="remark"]').send_keys(remark)
        self.driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        self.assertEqual(self.driver.switch_to.alert.text,result,msg="保存失败")


if __name__ == '__main__':
    unittest.main()
