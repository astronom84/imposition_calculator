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
        target = [
                {'number_of_pages': 4, 'pages_per_sheet': 4, 'sheets':
                                                    [
                                                       {
                                                        'front': [1, 4],
                                                        'back':  [2, 3]
                                                       }
                                                    ]
                   },
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
      {'number_of_pages': 32, 'pages_per_sheet': 32, 'sheets':
          [
             {
              'front': [1, 32, 16, 17, 8, 25, 9, 24, 4, 29, 13, 20, 5, 28, 12, 21],
              'back':  [2, 31, 15, 18, 7, 26, 10, 23, 3, 30, 14, 19, 6, 27, 11, 22]
             }
          ]
      }
              ]
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(t['number_of_pages'], t['pages_per_sheet'])
                self.assertListEqual(t['sheets'], gen.generate())


if __name__ == '__main__':
    unittest.main()

