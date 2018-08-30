class MainPage(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_search_query(self, query):
        search_input = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//input[contains(@class, 'search-input')]")
        search_input.clear()
        search_input.send_keys(query)

    def click_search_button(self):
        search_button = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//button[contains(@class, 'search-btn')]")
        search_button.click()