import unittest
import json
from imp_calculator import ImpCalculator

class ImpCalculator_TestCase(unittest.TestCase):
    def test_init(self):
        target= dict(number_of_pages=24, first_page=1, last_page=24, pages_per_sheet=8,
                     runs=1, nesting=1, half_sheet=0, _pages_per_sheet_side=4)
        gen = ImpCalculator(target['number_of_pages'], target['pages_per_sheet'], target['first_page'], target['last_page'], target['runs'], target['nesting'], target['half_sheet'])
        self.assertDictEqual(target, gen.__dict__)

    def test_init_last_page_is_empty(self):
        target = {'first_page': 1, 'last_page': 8}
        gen = ImpCalculator(number_of_pages=8, pages_per_sheet=8, first_page=target['first_page'], runs=1, nesting=1)
        res = {'first_page': gen.first_page, 'last_page': gen.last_page}
        self.assertDictEqual(target, res)

    def test_init_last_page_is_empty_first_page_big(self):
        target = {'first_page': 9, 'last_page': 16}
        gen = ImpCalculator(number_of_pages=8, pages_per_sheet=8, first_page=target['first_page'], runs=1, nesting=1)
        res = {'first_page': gen.first_page, 'last_page': gen.last_page}
        self.assertDictEqual(target, res)

    def test_init_last_page_gt_first_page(self):
        target = {'first_page': 1, 'last_page': 8}
        gen = ImpCalculator(number_of_pages=8, pages_per_sheet=8, first_page=target['last_page'], last_page=target['first_page'], runs=1, nesting=1)
        res = {'first_page': gen.first_page, 'last_page': gen.last_page}
        self.assertDictEqual(target, res)

    def test_pages_per_sheet(self):
        target = {2: 2, 4: 4, 8: 8, 16: 16, 32: 32, 64: 64}
        result = {}
        gen = ImpCalculator(8, 8, 1, 8, 1, 0)
        for i in target.keys():
            gen.pages_per_sheet = i
            result[i] = gen.pages_per_sheet
        self.assertDictEqual(target, result)

    def test_generate(self):
        data_files = ("test_data/test_A1_general.json",
                      "test_data/test_A2_general.json",
                      "test_data/test_A3_general.json",
                      "test_data/test_A3_half.json",
                      "test_data/test_A3_nesting.json")
        for filename in data_files:
            with open(filename) as a1test:
                test_values = json.load(a1test)
            params = test_values[0]
            for i in range(1, len(test_values)):
                params.update(test_values[i])
                gen = ImpCalculator(
                                    number_of_pages=params['number_of_pages'],
                                    pages_per_sheet=params['pages_per_sheet'],
                                    first_page=params['first_page'],
                                    last_page=params['last_page'],
                                    runs=params['runs'],
                                    nesting=params['nesting'],
                                    half_sheet=params['half_sheet']
                                    )
                target = params['sheets']
                result = gen.generate()
                self.assertListEqual(target, result)
