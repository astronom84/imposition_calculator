import unittest
from imposition_calculator import ImpCalculator

class MyTestCase(unittest.TestCase):
    def test_generate(self):
        target = [
            # A4
            {'number_of_pages': 16, 'pages_per_sheet': 16, 'sheets':
                [
                    {
                        'front': [1, 16, 8, 9, 4, 13, 5, 12],
                        'back': [2, 15, 7, 10, 3, 14, 6, 11]
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
