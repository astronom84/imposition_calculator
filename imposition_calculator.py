import  math
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


# TODO добавить проверку входных параметров: number_of_pages, pages_per_sheet, runs должны быть больше 1

class ImpCalculator:

    def __init__(self, number_of_pages: int, pages_per_sheet: int, first_page: int = 1,
    last_page: int = None, runs : int = 1, nesting: int = 1) -> None:
        self.number_of_pages = number_of_pages
        self.pages_per_sheet = pages_per_sheet
        self.first_page = first_page
        self.last_page = last_page
        self.runs = runs
        # nesting - количество газет в одной тетради (при печати "две в одной" nesting = 2)
        self.nesting = nesting

    @property
    def pages(self):
        full_length = math.ceil(self.number_of_pages/self.pages_per_sheet)*self.pages_per_sheet
        blank_elements = [[0]]*(full_length - self.number_of_pages)
        full_seq = [[i] for i in range(1, self.number_of_pages+1)] + blank_elements
        # центральный разворот
        central_spread = math.ceil(len(full_seq)//2)
        pages = full_seq[:central_spread]*self.nesting + full_seq[central_spread:]*self.nesting
        return pages

    @property
    def sections(self):
        sections = self.pages[:]
        folds = int(math.log2(self.pages_per_sheet)) - 1
        for _ in  range(folds):
            sections=[(sections[i]+sections.pop()) for i in range(len(sections)//2)]
        return sections 

    @property
    def sheets(self):
        sections = self.sections[:]
        sheets = [{"front": sections[i], "back":
                    sections[i+1]} for i in range(0, len(sections), 2)]
        return sheets

    def generate(self):
        return (self.sheets)

if __name__ == '__main__':
    params = cli_parse()
    if params:
        gen = ImpCalculator(params.number_of_pages, params.pages_per_sheet,
        params.first_page, params.last_page, params.signatures, params.nesting)
        result = gen.generate()
        for i in range(len(result)):
            print(f"sheet {i+1}: front={result[i]['front']}, back={result[i]['back']}")
