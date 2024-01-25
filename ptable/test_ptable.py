import pytest
import time
from _pytest.fixtures import FixtureRequest
from tabulate import tabulate


class ChemicalElement:
    def __init__(self, atomic: int, name: str, weight: float):
        self.atomic = atomic
        self.name = name
        self.weight = weight


class TestPTable:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.main_page = (request.getfixturevalue('main_page'))

    def test_ptable_elements(self):
        time.sleep(1)
        self.main_page.click(self.main_page.locators.WEIGHT_BTN)
        elements = self.main_page.find_all(self.main_page.locators.MAIN_TABLE_ELEMENTS)

        elements_objs = []
        for el in elements:
            atomic, abbr, name, weight = el.text.split('\n')
            elements_objs.append(ChemicalElement(int(atomic), name, float(weight.replace(',', '.'))))

        print(tabulate([vars(i).values() for i in elements_objs],
                       headers=['Atomic', 'Name', 'Weight'], tablefmt='orgtbl'))
