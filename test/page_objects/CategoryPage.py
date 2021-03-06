from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryPage(object):

    def __init__(self, driver):
        self.driver = driver

    def discard_cookie_banner(self):
        close_cookie_button = self.driver.find_element_by_xpath("//div[@id='cookie']//span[contains(@class, 'close')]")

        if close_cookie_button:
            close_cookie_button.click()

        return self

    def click_notify_me_about_availability(self):
        availability_notifier_button = self.driver.find_element_by_xpath("(//form[contains(@class, 'availability-notifier')] //button[contains(@class, 'availability-notifier-btn')])[1]")
        availability_notifier_button.click()
        return self

    def expect_availability_notifier_modal(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-visible')]//h3[contains(text(), 'Powiadom mnie o dostępności')]"))
            )
        except:
            pass

        return self

    def fill_in_availability_notifier_email(self, email):
        email_input = self.driver.find_element_by_xpath("//p/input")
        email_input.send_keys(email)
        return self

    def click_availability_notifier_add_me_button(self):
        add_email_button = self.driver.find_element_by_xpath("//p/button[contains(@class, 'btn btn-red')]")
        add_email_button.click()
        return self

    def expect_availability_notifier_success_confirmation(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-alert')]"))
            )
        except:
            pass

        return self

    def add_available_item_to_cart(self):
        add_to_cart = self.driver.find_element_by_xpath("(//form//button[contains(@class, 'addtobasket')])[1]")
        add_to_cart.click()
        return self

    def expect_add_to_cart_success_modal(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-header')]//span[contains(text(), 'Pomyślnie dodano do koszyka')]"))
            )
        except:
            pass

    def click_continue_shopping_button(self):
        continue_button = self.driver.find_element_by_xpath("//div[contains(@class, 'ajax-product-block')]/a[contains(@class, 'btn left')]")
        continue_button.click()

    def click_go_to_cart_button(self):
        cart_button = self.driver.find_element_by_xpath("//div[contains(@class, 'basket')]/a[contains(@class, 'count')]")
        cart_button.click()
