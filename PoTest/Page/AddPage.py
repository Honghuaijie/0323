from PoTest.Page.BasePage import BasePage

class AddPage(BasePage):
    pp_tag="品牌"
    xz_tag='//*[@id="content"]/div[2]/div/div[1]/button'
    pp_title="title"
    pp_code="code"
    pp_sub='//*[@id="submitButton"]'

    def AP_ppTag(self):
        self.linkTest(self.pp_tag).click()

    def AP_xzTag(self):
        self.xpath(self.xz_tag).click()

    def AP_code(self,code):
        self.id(self.pp_code).send_keys(code)

    def AP_title(self,title):
        self.id(self.pp_title).send_keys(title)

    def AP_sub(self):
        self.xpath(self.pp_sub).click()
