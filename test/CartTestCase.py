import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def prepare_cart(self):
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

        availability_notifier_button = self.driver.find_element_by_xpath("(//form[contains(@class, 'availability-notifier')] //button[contains(@class, 'availability-notifier-btn')])[2]")
        availability_notifier_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-visible')]//h3[contains(text(), 'Powiadom mnie o dostępności')]"))
            )
        except:
            pass
        
        add_email_button = self.driver.find_element_by_xpath("//p/button[contains(@class, 'btn btn-red')]")
        email_input = self.driver.find_element_by_xpath("//p/input")
        email_input.send_keys("katarzyna@op.pl")
        add_email_button.click()


        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-alert')]"))
            )
        except:
            pass

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
        open_cart = self.driver.find_element_by_xpath("//div[contains(@class, 'basket-contain')]//a[contains(text(), 'do kasy')]")
        open_cart.click()

    def test_search(self):

        self.driver.get("https://lawendowaszafa24.pl/")
        search_button = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//button[contains(@class, 'search-btn')]")
        search_input = self.driver.find_element_by_xpath("//form[contains(@class, 'search-form')]//input[contains(@class, 'search-input')]")
        search_input.clear()
        search_input.send_keys("balsam")
        search_button.click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'boxhead')]/h1[contains(text(), 'Znaleziono produktów')]"))
            )
        except:
            pass



        


