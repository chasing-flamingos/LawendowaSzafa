from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def expect_search_results_table(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'boxhead')]/h1[contains(text(), 'Znaleziono produktów')]"))
            )
        except:
            pass