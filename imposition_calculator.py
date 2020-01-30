"""
Модуль для вычисления раскладки по заданным критериям.
Требует Python 3.6+
Использование:
    $ python3 imposition_calculator.py -np <число страниц в издании> -pps <число
    страниц на лист>
Остальные аргументы являются опциональными.
Все аргументы целочисленные.
"""

import math
import argparse


class ImpCalculator:
    """ Класс, вычисляющий раскладку страниц макета."""

    def __init__(self,
                 number_of_pages: int,
                 pages_per_sheet: int,
                 first_page: int = 1,
                 last_page: int = 0,
                 runs: int = 1,
                 nesting: int = 1,
                 half_sheet: int = 0) -> None:
        """Инициализация экземпляра класса ImpCalculator

        Args:
            number_of_pages (int): количество страниц в издании
            pages_per_sheet (int): количество страниц на одном листе
            first_page (int): номер первой страницы
            last_page (int): номер последней страницы
            runs (int): количество прогонов (тетрадей)
            nesting (int): вложенность, количество копий издания в одной тетради
            half_sheet (int): номер листа половинки

        Returns:
            None
        """

        self.number_of_pages = number_of_pages
        self.pages_per_sheet = pages_per_sheet
        if last_page:
            self.first_page = min(first_page, last_page)
            self.last_page = max(last_page, first_page)
        else:
            self.first_page = first_page
            self.last_page = self.first_page + self.number_of_pages - 1
        self.runs = runs
        self.nesting = nesting or 1
        self.half_sheet = half_sheet

    @property
    def pages(self):
        """ Атрибут класса, содержащий список номеров страниц.
        Длина списка кратна параметру pages_per_sheet
            Returns:
                Список страниц
        """
        align = self.pages_per_sheet // 2
        number_of_pages = (math.ceil(self.number_of_pages/align)*align)
        if (self.last_page - self.first_page) < number_of_pages-1:
            result = list(range(self.first_page, self.last_page+1))
            result += [0]*(number_of_pages-len(result))
        else:
            result = [0]*number_of_pages
            middle = len(result) // 2
            for i in range(middle):
                result[i] = self.first_page + i
                result[-(i+1)] = self.last_page - i
#        print(f"pages = {result}")
        return result

    @property
    def sheets(self):
        """ Атрибут класса, содержащий список словарей, соответствующих листам.
            Returns:
                Список листов раскладки
        """
        quarters = [[x] for x in self.pages[:]]
#        print(f"quarters = {quarters}")
        if len(quarters[0]) <= self.pages_per_sheet // 4:
            folds = int(math.log2(self.pages_per_sheet//2)) - 1
            for _ in range(folds):
                quarters = [quarters[i] + quarters.pop() for i in range(len(quarters)//2)]
            if self.half_sheet:
                blank_pages = [0]*len(quarters[0])
                quarters.insert(2*(self.half_sheet-1), blank_pages)
                quarters.insert(2*(self.half_sheet-1), blank_pages)
            halves = [quarters[i] + quarters.pop() for i in range(len(quarters)//2)]
        else:
            halves = quarters
        result = [{"front": halves[i], "back": halves[i+1]} for i in range(0, len(halves), 2)]
#        print(f"sheets = {result}")
        return result

    def generate(self):
        """ Метод возвращает список листов вычисленной раскладки
            Returns:
                Список листов раскладки
        """
        return self.sheets


def main():
    """
    Функция для запуска приложения из командной строки.
    Функция
    - разбирает аргументы командной строки,
    - создает объект ImpCalculator с полученными аргументами командной строки,
    - вызывает метод generate() созданного объекта
    - выводит на экран результат вызова метода generate
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-np', '--number_of_pages', required=True, type=int)
    parser.add_argument('-pps', '--pages_per_sheet', required=True, type=int)
    parser.add_argument('-fp', '--first_page', default=1, type=int)
    parser.add_argument('-lp', '--last_page', type=int)
    parser.add_argument('-ns', '--signatures', default=1, type=int)
    parser.add_argument('-nt', '--nesting', default=1, type=int)
    parser.add_argument('-hs', '--half_sheet', type=int)
    params = parser.parse_args()
    if params:
        gen = ImpCalculator(params.number_of_pages,
                            params.pages_per_sheet,
                            params.first_page,
                            params.last_page,
                            params.signatures,
                            params.nesting)
        result = gen.generate()
        for i, sheet in enumerate(result):
            print(f"sheet {i+1}: front={sheet['front']}, back={sheet['back']}")


if __name__ == '__main__':
    main()
