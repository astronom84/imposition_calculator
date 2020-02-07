import unittest
from imposition_calculator import ImpCalculator

class MyTestCase(unittest.TestCase):

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

    def test_generate(self):
        target = [
                # A3
                {'number_of_pages': 8, 'pages_per_sheet': 8, 'sheets':
                    [
                        {
                            'front': [1, 8, 4, 5],
                            'back': [2, 7, 3, 6]
                        }
                    ]
                 },
                # A3 7 pages
                {'number_of_pages': 7, 'pages_per_sheet': 8, 'sheets':
                    [
                        {
                            'front': [1, 0, 4, 5],
                            'back': [2, 7, 3, 6]
                        }
                    ]
                 },
              ] # end list target
        result = []
        for t in target:
            with self.subTest(t=t):
                gen = ImpCalculator(t['number_of_pages'], t['pages_per_sheet'])
                self.assertListEqual(t['sheets'], gen.generate())


if __name__ == '__main__':
    unittest.main()
