import unittest
from imposition_calculator import ImpCalculator

class MyTestCase(unittest.TestCase):
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
             }
        ]  # end list target
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(t['number_of_pages'], t['pages_per_sheet'])
                self.assertListEqual(t['sheets'], gen.generate())

if __name__ == '__main__':
    unittest.main()
