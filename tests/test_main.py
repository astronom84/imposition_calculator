import unittest
from imposition_calculator import ImpGenerator


class ImpGenerator_TestCase(unittest.TestCase):
    def test_init(self):
        target = dict(pages=24, first_page=1, last_page=24, fmt=3, runs=1, double=False)
        gen = ImpGenerator(target['pages'], target['first_page'], target['last_page'], target['fmt'], target['runs'], target['double'])
        self.assertDictEqual(target, gen.__dict__)

    def test_pages_per_sheet(self):
        target = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64}
        result = {}
        gen = ImpGenerator(8, 1, 8, 1, 1, False)
        for i in target.keys():
            gen.fmt = i
            result[i] = gen.pages_per_sheet
        self.assertDictEqual(target, result)

    def test_generate(self):
        target = [{'pages': 4, 'fmt': 2, 'sections': [(1, 4), (2, 3)]},
#                  {'pages': 4, 'fmt': 3, 'sections': [((0, 0), (2, 3)), ((0, 0), (1, 4))]},
                  {'pages': 8, 'fmt': 3, 'sections': [((1, 8), (4, 5)), ((2, 7), (3, 6))]},
                  {'pages': 7, 'fmt': 3, 'sections': [((1, 0), (4, 5)), ((2, 7), (3, 6))]},
                  {'pages': 16, 'fmt': 4, 'sections': [
                  (((1, 16), (8, 9)), ((4, 13),(5, 12))),
                  (((2, 15), (7, 10)), ((3, 14),(6, 11))),
                  ]},
                 ]
        result = []
        gen = ImpGenerator(8, 1, 8, 1, 1, False)
        for t in target:
            gen.pages = t['pages']
            gen.fmt = t['fmt']
            result.append({'pages': gen.pages, 'fmt': gen.fmt, 'sections': gen.generate()})
        self.assertListEqual(target, result)


if __name__ == '__main__':
    unittest.main()

