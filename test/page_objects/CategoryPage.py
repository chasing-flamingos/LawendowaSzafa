class CategoryPage(object):

    def __init__(self, driver):
        self.driver = driver

    def discard_cookie_banner(self):
        close_cookie_button = self.driver.find_element_by_xpath("//div[@id='cookie']//span[contains(@class, 'close')]")

        if close_cookie_button:
            close_cookie_button.click()