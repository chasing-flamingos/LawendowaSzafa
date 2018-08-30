from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(object):

    def __init__(self, driver):
        self.driver = driver

    def expect_products_table(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'basket-contain')]"))
            )
        except:
            pass

    def expect_products_table_item_count_to_be(self, n):
        products = self.driver.find_elements_by_xpath("//table[contains(@class, 'productlist')]/tbody/tr")
        assert len(products) == n

    def click_remove_product_from_cart(self):
        remove_button = self.driver.find_element_by_xpath("(//td[@class='actions']/a[@class='prodremove'])[1]")
        remove_button.click()