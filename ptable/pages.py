from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PtablePageLocators


class PtablePage(object):
    locators = PtablePageLocators
    url = 'https://ptable.com/'

    def __init__(self, driver):
        self.driver = driver
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def wait(self, timeout=None) -> WebDriverWait:
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None) -> list[WebElement]:
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator, timeout=None) -> None:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
