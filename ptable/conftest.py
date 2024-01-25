import pytest
from selenium import webdriver
from pages import PtablePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return PtablePage(driver)
