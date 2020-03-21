"""
Использование:
    $ python3 cli.py -np <число страниц в издании> -pps <число
    страниц на лист>
Остальные аргументы являются опциональными.
Все аргументы целочисленные.
"""

import argparse
from imp_calculator.imp_calculator import ImpCalculator

def cli():
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
                            params.nesting,
                            params.half_sheet)
        result = gen.generate()
        for i, sheet in enumerate(result):
            print(f"sheet {i+1}: front={sheet['front']}, back={sheet['back']}")


if __name__ == '__main__':
    cli()
