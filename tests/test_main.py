import unittest
from imposition_calculator import ImpCalculator


class ImpCalculator_TestCase(unittest.TestCase):
    def test_init(self):
        target= dict(number_of_pages=24, first_page=1, last_page=24, pages_per_sheet=8,
        runs=1, nesting=1, half_sheet=0, _pages_per_section=4)
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
            {'number_of_pages': 2, 'pages_per_sheet': 2, 'sheets':
                [
                    {
                        'front': [1],
                        'back': [2]
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

    def test_generate_4A3_half_1(self):
        target = [
                    {
                        'front': [0, 0, 2, 3],
                        'back':  [0, 0, 1, 4]
                    },
                  ]
        gen = ImpCalculator(4, 8, 1, 4, 1, 0, 1)
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

    def test_generate_8A3_2in1(self):
        target = [
                    {
                        'front': [1, 8, 4, 5],
                        'back':  [2, 7, 3, 6]
                    },
                    {
                        'front':  [3, 6, 2, 7],
                        'back': [4, 5, 1, 8]
                    }
                  ]
        gen = ImpCalculator(8, 8, 1, 8, 1, 2)
        self.assertListEqual(target, gen.generate())

    def test_generate_A2(self):
        pages_per_sheet = 4
        target = [
                     {
                         'number_of_pages': 1,
                         'first_page': 1,
                         'last_page': 1,
                         'nesting': 1,
                         'half_sheet': 1,
                         'sheets':
                                 [
                                     {
                                         'front': [0, 0],
                                         'back':  [0, 1]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 2,
                         'first_page': 1,
                         'last_page': 2,
                         'nesting': 1,
                         'half_sheet': 1,
                         'sheets':
                                 [
                                     {
                                         'front': [0, 2],
                                         'back':  [0, 1]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 3,
                         'first_page': 1,
                         'last_page': 3,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 3]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 4,
                         'first_page': 1,
                         'last_page': 4,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 4],
                                         'back':  [2, 3]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 5,
                         'first_page': 1,
                         'last_page': 5,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 5]
                                     },
                                     {
                                         'front': [0, 4],
                                         'back':  [0, 3]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 6,
                         'first_page': 1,
                         'last_page': 6,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 6],
                                         'back':  [2, 5]
                                     },
                                     {
                                         'front': [0, 4],
                                         'back':  [0, 3]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 7,
                         'first_page': 1,
                         'last_page': 7,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 7]
                                     },
                                     {
                                         'front': [3, 6],
                                         'back':  [4, 5]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 8,
                         'first_page': 1,
                         'last_page': 8,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 8],
                                         'back':  [2, 7]
                                     },
                                     {
                                         'front': [3, 6],
                                         'back':  [4, 5]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 9,
                         'first_page': 1,
                         'last_page': 9,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 9]
                                     },
                                     {
                                         'front': [3, 8],
                                         'back':  [4, 7]
                                     },
                                     {
                                         'front': [0, 6],
                                         'back':  [0, 5]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 10,
                         'first_page': 1,
                         'last_page': 10,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 10],
                                         'back':  [2, 9]
                                     },
                                     {
                                         'front': [3, 8],
                                         'back':  [4, 7]
                                     },
                                     {
                                         'front': [0, 6],
                                         'back':  [0, 5]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 11,
                         'first_page': 1,
                         'last_page': 11,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 11]
                                     },
                                     {
                                         'front': [3, 10],
                                         'back':  [4, 9]
                                     },
                                     {
                                         'front': [5, 8],
                                         'back':  [6, 7]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 12,
                         'first_page': 1,
                         'last_page': 12,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 12],
                                         'back':  [2, 11]
                                     },
                                     {
                                         'front': [3, 10],
                                         'back':  [4, 9]
                                     },
                                     {
                                         'front': [5, 8],
                                         'back':  [6, 7]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 13,
                         'first_page': 1,
                         'last_page': 13,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 13]
                                     },
                                     {
                                         'front': [3, 12],
                                         'back':  [4, 11]
                                     },
                                     {
                                         'front': [5, 10],
                                         'back':  [6, 9]
                                     },
                                     {
                                         'front': [0, 8],
                                         'back':  [0, 7]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 14,
                         'first_page': 1,
                         'last_page': 14,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 14],
                                         'back':  [2, 13]
                                     },
                                     {
                                         'front': [3, 12],
                                         'back':  [4, 11]
                                     },
                                     {
                                         'front': [5, 10],
                                         'back':  [6, 9]
                                     },
                                     {
                                         'front': [0, 8],
                                         'back':  [0, 7]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 15,
                         'first_page': 1,
                         'last_page': 15,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 15]
                                     },
                                     {
                                         'front': [3, 14],
                                         'back':  [4, 13]
                                     },
                                     {
                                         'front': [5, 12],
                                         'back':  [6, 11]
                                     },
                                     {
                                         'front': [7, 10],
                                         'back':  [8, 9]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 16,
                         'first_page': 1,
                         'last_page': 16,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 16],
                                         'back':  [2, 15]
                                     },
                                     {
                                         'front': [3, 14],
                                         'back':  [4, 13]
                                     },
                                     {
                                         'front': [5, 12],
                                         'back':  [6, 11]
                                     },
                                     {
                                         'front': [7, 10],
                                         'back':  [8, 9]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 17,
                         'first_page': 1,
                         'last_page': 17,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 17]
                                     },
                                     {
                                         'front': [3, 16],
                                         'back':  [4, 15]
                                     },
                                     {
                                         'front': [5, 14],
                                         'back':  [6, 13]
                                     },
                                     {
                                         'front': [7, 12],
                                         'back':  [8, 11]
                                     },
                                     {
                                         'front': [0, 10],
                                         'back':  [0, 9]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 18,
                         'first_page': 1,
                         'last_page': 18,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 18],
                                         'back':  [2, 17]
                                     },
                                     {
                                         'front': [3, 16],
                                         'back':  [4, 15]
                                     },
                                     {
                                         'front': [5, 14],
                                         'back':  [6, 13]
                                     },
                                     {
                                         'front': [7, 12],
                                         'back':  [8, 11]
                                     },
                                     {
                                         'front': [0, 10],
                                         'back':  [0, 9]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 19,
                         'first_page': 1,
                         'last_page': 19,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 0],
                                         'back':  [2, 19]
                                     },
                                     {
                                         'front': [3, 18],
                                         'back':  [4, 17]
                                     },
                                     {
                                         'front': [5, 16],
                                         'back':  [6, 15]
                                     },
                                     {
                                         'front': [7, 14],
                                         'back':  [8, 13]
                                     },
                                     {
                                         'front': [9, 12],
                                         'back':  [10, 11]
                                     }
                                 ]
                     },
                     {
                         'number_of_pages': 20,
                         'first_page': 1,
                         'last_page': 20,
                         'nesting': 1,
                         'half_sheet': 0,
                         'sheets':
                                 [
                                     {
                                         'front': [1, 20],
                                         'back':  [2, 19]
                                     },
                                     {
                                         'front': [3, 18],
                                         'back':  [4, 17]
                                     },
                                     {
                                         'front': [5, 16],
                                         'back':  [6, 15]
                                     },
                                     {
                                         'front': [7, 14],
                                         'back':  [8, 13]
                                     },
                                     {
                                         'front': [9, 12],
                                         'back':  [10, 11]
                                     }
                                 ]
                     },
                 ]
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(
                            number_of_pages = t['number_of_pages'],
                            pages_per_sheet = pages_per_sheet,
                            first_page = t['first_page'],
                            last_page = t['last_page'],
                            nesting = t['nesting'],
                            half_sheet = t['half_sheet']
                            )
                self.assertListEqual(t['sheets'], gen.generate())


if __name__ == '__main__':
    unittest.main()

