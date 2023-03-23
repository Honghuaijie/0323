from PoTest.Page.BasePage import BasePage

class LoginPage(BasePage):
    url="http://www.rjcs.site:8888/pams"
    loginName="loginName"
    passwd="password"
    tag="button"
    def open(self):
        self.get(self.url)

    def LP_loginName(self,loginName):
        self.id(self.loginName).send_keys(loginName)

    def LP_passwd(self,password):
        self.id(self.passwd).send_keys(password)

    def LP_login(self):
        self.tag_name(self.tag).click()