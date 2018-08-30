from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(object):

    def __init__(self, driver):
        self.driver = driver

    def select_product_count(self, n):
        amount_input = self.driver.find_element_by_xpath("//div[contains(@class, 'quantity_wrap')]//input[contains(@class, 'short')]")
        amount_input.clear()
        amount_input.send_keys(n)

    def click_add_to_cart_button(self):
        add_to_cart_button = self.driver.find_element_by_xpath("//form//div[contains(@class, 'button_wrap')]/button[contains(@class, 'addtobasket')]")
        add_to_cart_button.click()

    def expect_add_to_cart_success_modal(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-header')]//span[contains(text(), 'Pomyślnie dodano do koszyka')]"))
            )
        except:
            pass