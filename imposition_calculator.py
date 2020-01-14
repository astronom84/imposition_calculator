from math import ceil

# TODO добавить проверку входных параметров: pages, fmt, runs должны быть больше 1
class ImpGenerator:

    def __init__(self, pages: int = 8, first_page: int = 1, last_page: int = None, fmt: int = 3, runs: int = 1, nesting: int = 1) -> None:
        self.pages = pages
        self.fmt = fmt
        self.runs = runs
        # nestin - количество газет в одной тетради (при печати "две в одной" nesting = 2)
        self.nesting = nesting
        self.first_page = first_page
        if last_page > 0:
            self.last_page = last_page
        else:
            self.last_page = self.pages

    @property
    def pages_per_sheet(self):
        return 2**self.fmt

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
