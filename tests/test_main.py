import unittest
from imposition_calculator import ImpCalculator


class ImpCalculator_TestCase(unittest.TestCase):
    def test_init(self):
        target= dict(number_of_pages=24, first_page=1, last_page=24, pages_per_sheet=8,
        runs=1, nesting=1)
        gen = ImpCalculator(target['number_of_pages'], target['pages_per_sheet'], target['first_page'], target['last_page'], target['runs'], target['nesting'])
        self.assertDictEqual(target, gen.__dict__)

    def test_pages_per_sheet(self):
        target = {2: 2, 4: 4, 8: 8, 16: 16, 32: 32, 64: 64}
        result = {}
        gen = ImpCalculator(8, 8, 1, 8, 1, False)
        for i in target.keys():
            gen.pages_per_sheet = i
            result[i] = gen.pages_per_sheet
        self.assertDictEqual(target, result)

    def test_generate(self):
        target = [{'number_of_pages': 4, 'pages_per_sheet': 4, 'sheets':
                                                    [
                                                       {
                                                        'front': [1, 4],
                                                        'back':  [2, 3]
                                                       }
                                                    ]
                   },
#                  {'number_of_pages': 4, 'pages_per_sheet': 8, 'sheets': 
#                                                    [
#                                                       {
#                                                        'front': [0, 0, 2, 3],
#                                                        'back':  [0, 0, 1, 4]
#                                                       }
#                                                    ]
#                   }, 
                  {'number_of_pages': 8, 'pages_per_sheet': 8, 'sheets':
                                                    [
                                                       {
                                                        'front': [1, 8, 4, 5],
                                                        'back':  [2, 7, 3, 6]
                                                       }
                                                    ]
                  },
                  {'number_of_pages': 7, 'pages_per_sheet': 8, 'sheets':
                                                    [
                                                       {
                                                        'front': [1, 0, 4, 5],
                                                        'back':  [2, 7, 3, 6]
                                                       }
                                                    ]
                  },
                  {'number_of_pages': 16, 'pages_per_sheet': 16, 'sheets':
                                      [
                                         {
                                           'front': [1, 16, 8, 9, 4, 13, 5, 12],
                                           'back':  [2, 15, 7, 10, 3, 14, 6, 11]
                                         }
                                      ]
                 },
                 ]
        result = []
        gen = ImpCalculator(8, 8, 1, 8, 1, 1)
        for t in target:
            gen.number_of_pages = t['number_of_pages']
            gen.pages_per_sheet = t['pages_per_sheet']
            result.append({'number_of_pages': gen.number_of_pages, 'pages_per_sheet': gen.pages_per_sheet, 'sheets': gen.generate()})
        self.assertListEqual(target, result)


if __name__ == '__main__':
    unittest.main()

