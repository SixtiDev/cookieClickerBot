from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

WEBDRIVER_PATH = "C:\SynologyDrive\Projekty\chromedriver\chromedriver.exe"


class CookieWebdriver:

    def __init__(self):
        service = Service(WEBDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.open_game()
        self.cookie_button = self.driver.find_element(By.ID, "bigCookie")
        self.clickable_upgrades = []
        self.clickable_products = []

    def open_game(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")

    def close_game(self):
        self.driver.quit()

    def find_cookie(self):
        self.cookie_button = self.driver.find_element(By.ID, "bigCookie")

    def click_cookie(self):
        self.cookie_button.click()

    def find_clickable_upgrades(self):
        self.clickable_upgrades = self.driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")

    def find_clickable_products(self):
        self.clickable_products = self.driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    def is_upgrade_available(self):
        if self.clickable_upgrades:
            print("Found clickable upgrade")
            return True
        else:
            print("No clickable upgrade")
            return False

    def is_product_available(self):
        if self.clickable_products:
            print("Found clickable products")
            return True
        else:
            print("No clickable products")
            return False

    def update_and_check_upgrades(self):
        self.find_clickable_upgrades()
        return self.is_upgrade_available()

    def update_and_check_products(self):
        self.find_clickable_products()
        return self.is_product_available()

    def buy_upgrades(self):
        while self.update_and_check_upgrades():
            self.clickable_upgrades[0].click()
            print("Upgrade bought")
            self.driver.implicitly_wait(0.3)

    def buy_products(self):
        while self.update_and_check_products():
            self.clickable_products[-1].click()
            print("Product bought")
