import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from test.page_objects.CategoryPage import CategoryPage
from test.page_objects.CartPage import CartPage
from test.page_objects.ProductPage import ProductPage
from test.page_objects.MainPage import MainPage
from test.page_objects.SearchResultsPage import SearchResultsPage

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
        category_page.expect_add_to_cart_success_modal()
        category_page.click_continue_shopping_button()

    def tearDown(self):
        self.driver.close()

    def test_add_to_cart(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/DUETUS-Peeling-do-twarzy-75-ml-SYLVECO/5565")
        product_page = ProductPage(self.driver)
        product_page.select_product_count(1)
        product_page.click_add_to_cart_button()
        product_page.expect_add_to_cart_success_modal()

    def test_add_to_cart_zero_item(self):
        self.driver.get("https://lawendowaszafa24.pl/pl/p/Intensywny-krem-przeciwzmarszczkowy-do-twarzy-NIEDZWIEDZIA-SILA-dla-prawdziwych-mezczyzn-Natura-Siberica-MEN/2239")
        product_page = ProductPage(self.driver)
        product_page.select_product_count(0)
        product_page.click_add_to_cart_button()
        product_page.expect_add_to_cart_wrong_product_count_modal()

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

        category_page = CategoryPage(self.driver)
        category_page.click_go_to_cart_button()

        cart_page = CartPage(self.driver)
        cart_page.expect_products_table()
        
        time.sleep(5)

        cart_page.expect_products_table_item_count_to_be(1)

    def test_search(self):

        self.driver.get("https://lawendowaszafa24.pl/")
        main_page = MainPage(self.driver)
        main_page.enter_search_query("balsam")
        main_page.click_search_button()

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.expect_search_results_table()


    def test_remove_item_from_cart(self):

        self.prepare_cart()

        time.sleep(10)
        category_page = CategoryPage(self.driver)
        category_page.click_go_to_cart_button()

        cart_page = CartPage(self.driver)
        cart_page.expect_products_table()

        time.sleep(5)

        cart_page.expect_products_table_item_count_to_be(1)
        cart_page.click_remove_product_from_cart()
        cart_page.expect_products_table_item_count_to_be(0)


