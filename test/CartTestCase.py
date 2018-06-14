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
        
        add_to_cart_button = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]/button")
        amount_input = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[1]/span[2]/input")
        
        amount_input.clear()
        amount_input.send_keys("1")
        add_to_cart_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shop_product3138\"]/div[contains(@class, 'modal-visible')]"))
            )
        except:
            pass

        continue_button = self.driver.find_element_by_xpath("//div[contains(@class, 'modal-visible')]//a[contains(text(), 'Kontynuuj zakupy')]")
        continue_button.click()


    def tearDown(self):
        self.driver.close()

    def test_add_to_cart(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/Balsam-do-wlosow-nawilzajacy-do-wlosow-oslabionych-i-farbowanych%2C-400ml-Natura-Estonica-Bio/3138")
        
        add_to_cart_button = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]/button")
        amount_input = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[1]/span[2]/input")
        
        amount_input.clear()
        amount_input.send_keys("1")
        add_to_cart_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shop_product3138\"]/div[contains(@class, 'modal-visible')]"))
            )
        except:
            pass

    def test_add_to_cart_zero_item(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/Intensywny-krem-przeciwzmarszczkowy-do-twarzy-NIEDZWIEDZIA-SILA-dla-prawdziwych-mezczyzn-Natura-Siberica-MEN/2239")
        
        add_to_cart_button = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]/button")
        amount_input = self.driver.find_element_by_xpath("//*[@id=\"box_productfull\"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[1]/span[2]/input")
        
        amount_input.clear()
        amount_input.send_keys("0")
        add_to_cart_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shop_product2239\"]/div[15]"))
            )
        except:
            pass

    def test_add_to_cart_out_of_stock(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/c/PIELEGNACJA-WLOSOW/93")

        availability_notifier_button = self.driver.find_element_by_xpath("//*[@id=\"box_mainproducts\"]/div[2]/div[1]/div[11]/div/div[3]/form/fieldset/button")
        availability_notifier_button.click()

        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shop_category93\"]/div[12]"))
            )
        except:
            pass
        
        add_email_button = self.driver.find_element_by_xpath("//*[@id=\"shop_category93\"]/div[12]/div[2]/div/form/p[3]/button")
        email_input = self.driver.find_element_by_xpath("//*[@id=\"shop_category93\"]/div[12]/div[2]/div/form/p[3]/input")
        email_input.send_keys("katarzyna@op.pl")
        add_email_button.click()


        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shop_category93\"]/div[12]"))
            )
        except:
            pass

    def test_view_cart(self):
        
        self.prepare_cart()

        time.sleep(10)
        cart_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[1]/div[2]/a")
        cart_button.click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/header/div[2]"))
            )
        except:
            pass
        
        time.sleep(5)
        open_cart = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div[2]/a")
        open_cart.click()

    def test_search(self):

        self.driver.get("https://lawendowaszafa24.pl/")
        search_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[1]/form/fieldset/button")
        search_input = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[1]/form/fieldset/input")
        search_input.clear()
        search_input.send_keys("balsam")
        search_button.click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"box_mainproducts\"]/div[1]/h1"))
            )
        except:
            pass



        


