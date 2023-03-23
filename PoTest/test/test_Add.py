from PoTest.Page.LoginPage import LoginPage
from PoTest.Page.AddPage import AddPage
from selenium import webdriver
import unittest

class Test02(unittest.TestCase):

    def test01(self):
        self.driver = webdriver.Chrome()
        self.LP=LoginPage(self.driver)
        self.AP=AddPage(self.driver)

        self.LP.open()
        self.LP.LP_loginName("njkjxn")
        self.LP.LP_passwd("student")
        self.LP.LP_login()

        print(123)
        self.AP.AP_ppTag()
        self.AP.AP_xzTag()
        self.AP.AP_title("0205")
        self.AP.AP_code("cpde0205")
        self.AP.AP_sub()


if __name__ == '__main__':
    unittest.main()
