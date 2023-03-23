class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.time=5

    def get(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(self.time)

    def xpath(self,url):
        return self.driver.find_element_by_xpath(url)

    def id(self,url):
        return self.driver.find_element_by_id(url)

    def tag_name(self,url):
        return self.driver.find_element_by_tag_name(url)

    def linkTest(self,url):
        return self.driver.find_element_by_link_text(url)
