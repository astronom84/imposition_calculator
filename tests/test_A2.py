import unittest
from imposition_calculator import ImpCalculator

class MyTestCase(unittest.TestCase):
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
