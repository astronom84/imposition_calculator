import unittest
from imposition_calculator import ImpCalculator


class ImpCalculator_TestCase(unittest.TestCase):
    def test_init(self):
        target= dict(number_of_pages=24, first_page=1, last_page=24, pages_per_sheet=8,
        runs=1, nesting=1, half_sheet=0)
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
        gen = ImpCalculator(8, 8, 1, 8, 1, False)
        for i in target.keys():
            gen.pages_per_sheet = i
            result[i] = gen.pages_per_sheet
        self.assertDictEqual(target, result)

    def test_generate(self):
        target = [
            # A1
#            {'number_of_pages': 2, 'pages_per_sheet': 2, 'sheets':
#                [
#                    {
#                        'front': [1],
#                        'back': [2]
#                    }
#                ]
#             },
                # A2
            {'number_of_pages': 4, 'pages_per_sheet': 4, 'sheets':
                [
                    {
                        'front': [1, 4],
                        'back':  [2, 3]
                    }
                ]
            },
            # A3
            {'number_of_pages': 8, 'pages_per_sheet': 8, 'sheets':
                [
                    {
                        'front': [1, 8, 4, 5],
                        'back':  [2, 7, 3, 6]
                    }
                ]
            },
            # A3 7 pages
            {'number_of_pages': 7, 'pages_per_sheet': 8, 'sheets':
                [
                    {
                        'front': [1, 0, 4, 5],
                        'back':  [2, 7, 3, 6]
                    }
                ]
            },
            # A4
            {'number_of_pages': 16, 'pages_per_sheet': 16, 'sheets':
                [
                    {
                        'front': [1, 16, 8, 9, 4, 13, 5, 12],
                        'back':  [2, 15, 7, 10, 3, 14, 6, 11]
                    }
                ]
            },
      # A5
      {'number_of_pages': 32, 'pages_per_sheet': 32, 'sheets':
          [
             {
              'front': [1, 32, 16, 17, 8, 25, 9, 24, 4, 29, 13, 20, 5, 28, 12, 21],
              'back':  [2, 31, 15, 18, 7, 26, 10, 23, 3, 30, 14, 19, 6, 27, 11, 22]
             }
          ]
      }
              ] # end list target
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(t['number_of_pages'], t['pages_per_sheet'])
                self.assertListEqual(t['sheets'], gen.generate())

    def test_generate_8A3_first_1_last_32(self):
        target = [
                    {
                        'front': [1, 32, 4, 29],
                        'back':  [2, 31, 3, 30]
                    }
                  ]
        gen = ImpCalculator(8, 8, 1, 32, 1, 0)
        self.assertListEqual(target, gen.generate())

    def test_generate_12A3_half_2(self):
        target = [
                    {
                        'front': [1, 12, 6, 7],
                        'back':  [2, 11, 5, 8]
                    },
                    {
                        'front': [0, 0, 4, 9],
                        'back':  [0, 0, 3, 10]
                    }
                  ]
        gen = ImpCalculator(12, 8, 1, 12, 1, 0, 2)
        self.assertListEqual(target, gen.generate())

if __name__ == '__main__':
    unittest.main()

