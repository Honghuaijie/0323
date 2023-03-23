from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.rjcs.site:8888/pams")
driver.find_element_by_name("loginName").send_keys("njkjxn")
driver.find_element_by_name("password").send_keys("student")
driver.find_element_by_tag_name("button").click()
driver.get_screenshot_as_file("denglu.png")
