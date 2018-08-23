import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from test.page_objects.CategoryPage import CategoryPage

class CartTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def prepare_cart(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/c/Anti-Hair-Loss/2912")
        category_page = CategoryPage(self.driver)
        category_page.discard_cookie_banner()
        category_page.add_available_item_to_cart()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-header')]//span[contains(text(), 'Pomyślnie dodano do koszyka')]"))
            )
        except:
            pass

        continue_button = self.driver.find_element_by_xpath("//div[contains(@class, 'ajax-product-block')]/a[contains(@class, 'btn left')]")
        continue_button.click()


    def tearDown(self):
        self.driver.close()

    def test_add_to_cart(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/Balsam-do-wlosow-nawilzajacy-do-wlosow-oslabionych-i-farbowanych%2C-400ml-Natura-Estonica-Bio/3138")
        
        add_to_cart_button = self.driver.find_element_by_xpath("//form//div[contains(@class, 'button_wrap')]/button[contains(@class, 'addtobasket')]")
        amount_input = self.driver.find_element_by_xpath("//div[contains(@class, 'quantity_wrap')]//input[contains(@class, 'short')]")
        
        amount_input.clear()
        amount_input.send_keys("1")
        add_to_cart_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-header')]//span[contains(text(), 'Pomyślnie dodano do koszyka')]"))
            )
        except:
            pass

    def test_add_to_cart_zero_item(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/Intensywny-krem-przeciwzmarszczkowy-do-twarzy-NIEDZWIEDZIA-SILA-dla-prawdziwych-mezczyzn-Natura-Siberica-MEN/2239")
        
        add_to_cart_button = self.driver.find_element_by_xpath("//form//div[contains(@class, 'button_wrap')]/button[contains(@class, 'addtobasket')]")
        amount_input = self.driver.find_element_by_xpath("//div[contains(@class, 'quantity_wrap')]//input[contains(@class, 'short')]")
        
        amount_input.clear()
        amount_input.send_keys("0")
        add_to_cart_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-alert')]//div[contains(text(), 'Nieprawidłowa ilość produktów.')]"))
            )
        except:
            pass

    def test_add_to_cart_out_of_stock(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/c/PIELEGNACJA-WLOSOW/93")

        CategoryPage(self.driver).discard_cookie_banner()                                   \
                                 .click_notify_me_about_availability()                      \
                                 .expect_availability_notifier_modal()                      \
                                 .fill_in_availability_notifier_email("katarzyna@op.pl")    \
                                 .click_availability_notifier_add_me_button()               \
                                 .expect_availability_notifier_success_confirmation()

    def test_view_cart(self):
        
        self.prepare_cart()

        time.sleep(10)
        cart_button = self.driver.find_element_by_xpath("//div[contains(@class, 'basket')]/a[contains(@class, 'count')]")
        cart_button.click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'basket-contain')]"))
            )
        except:
            pass
        
        time.sleep(5)
        products = self.driver.find_elements_by_xpath("//table[contains(@class, 'productlist')]/tbody/tr")
        assert len(products) == 1

    def test_search(self):

        self.driver.get("https://lawendowaszafa24.pl/")
        search_input = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//input[contains(@class, 'search-input')]")
        search_input.clear()
        search_input.send_keys("balsam")
        search_button = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//button[contains(@class, 'search-btn')]")
        search_button.click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'boxhead')]/h1[contains(text(), 'Znaleziono produktów')]"))
            )
        except:
            pass

    def test_product_preview(self):

        self.driver.get("https://lawendowaszafa24.pl/pl/c/PIELEGNACJA-WLOSOW/93")
        preview_button = self.driver.find_element_by_xpath("(//div[contains(@class, 'buttons f-row')]/a[contains(@class, 'btn large tablet quickview')])[1]")
        preview_button.click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-visible')]"))
            )
        except:
            pass

        close_button = self.driver.find_element_by_xpath("//div[@class='modal-close']/span[@class='modal-close-txt']")
        close_button.click()

    def test_remove_item_from_cart(self):

        self.prepare_cart()

        time.sleep(10)
        cart_button = self.driver.find_element_by_xpath("//div[contains(@class, 'basket')]/a[contains(@class, 'count')]")
        cart_button.click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'basket-contain')]"))
            )
        except:
            pass


        time.sleep(5)
        cart_button = self.driver.find_element_by_xpath("//div[contains(@class, 'basket')]/a[contains(@class, 'count')]")
        cart_button.click()

        remove_button = self.driver.find_element_by_xpath("(//td[@class='actions']/a[@class='prodremove'])[1]")
        remove_button.click()
        

