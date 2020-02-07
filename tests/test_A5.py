import unittest
from imposition_calculator import ImpCalculator

class MyTestCase(unittest.TestCase):
    def test_generate(self):
        target = [
            # A5
            {'number_of_pages': 32, 'pages_per_sheet': 32, 'sheets':
                [
                    {
                        'front': [1, 32, 16, 17, 8, 25, 9, 24, 4, 29, 13, 20, 5, 28, 12, 21],
                        'back': [2, 31, 15, 18, 7, 26, 10, 23, 3, 30, 14, 19, 6, 27, 11, 22]
                    }
                ]
             }
        ]  # end list target
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(t['number_of_pages'], t['pages_per_sheet'])
                self.assertListEqual(t['sheets'], gen.generate())


if __name__ == '__main__':
    unittest.main()
