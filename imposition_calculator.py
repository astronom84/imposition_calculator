from math import ceil
import argparse


def cli_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-np', '--number_of_pages', required=True, type=int)
    parser.add_argument('-pps', '--pages_per_sheet', required=True, type=int)
    parser.add_argument('-fp', '--first_page', default=1, type=int)
    parser.add_argument('-lp', '--last_page', type=int)
    parser.add_argument('-ns', '--signatures', default=1, type=int)
    parser.add_argument('-nt', '--nesting', default=1, type=int)
    parser.add_argument('-hs', '--half_sheet', type=int)
    return parser.parse_args()


# TODO добавить проверку входных параметров: pages, pages_per_sheet, runs должны быть больше 1

class ImpCalculator:

    def __init__(self, pages: int, pages_per_sheet: int, first_page: int = 1,
    last_page: int = None, runs : int = 1, nesting: int = 1) -> None:
        self.pages = pages
        self.pages_per_sheet = pages_per_sheet
        self.first_page = first_page
        self.last_page = last_page
        self.runs = runs
        # nesting - количество газет в одной тетради (при печати "две в одной" nesting = 2)
        self.nesting = nesting

    @property
    def sequence(self):
        full_length = ceil(self.pages/self.pages_per_sheet)*self.pages_per_sheet
        blank_elements = [0]*(full_length - self.pages)
        full_seq = list(range(1, self.pages+1)) + blank_elements
        # Номер первой страницы центрального разворота
        central_spread = ceil(len(full_seq) // 2)
        seq = full_seq[:central_spread]*self.nesting + full_seq[central_spread:]*self.nesting
        return seq

    def generate(self):
        pages = self.sequence
        count_of_sheets = len(pages) // self.pages_per_sheet
        while len(pages) > 2 * count_of_sheets:
            pages = [(pages[i], pages[-(i + 1)]) for i in range(len(pages) // 2)]
        return pages


if __name__ == '__main__':
    params = cli_parse()
    if params:
        gen = ImpCalculator(params.number_of_pages, params.pages_per_sheet,
        params.first_page, params.last_page, params.signatures, params.nesting)
        result = gen.generate()
        print(result)
