#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Zagadnienia dodatkowe
#
# -----------------------------------------------------------------------------

from typing import List, Set, Dict, Tuple, Optional, Callable


def get_unique_letters(s: str) -> Set[str]:
    """Zwróć zbiór unikalnych liter (o ile łańcuch zawiera co najmniej 3 znaki).

    Aby otrzymać listę znaków w łańcuchu znaków, przekaż ten łańcuch jako argument
    funkcji list().

    :param s:
    :return: zbiór unikalnych liter w łańcuchu znaków, jeśli łańcuch zawiera co
        najmniej 3 znaki, inaczej zbiór pusty
    """
    if len(s) >= 3:
        return set(s)
    return set()
    pass


# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def products_to_buy(list1: ShoppingList, list2: ShoppingList) -> Set[str]:
    """Zwróć zbiór produktów, które należy kupić.

    Przyjmij, że każda z list zawiera produkty, których należy kupić co najmniej
    jedną sztukę.

    W implementacji użyj wyłącznie instrukcji `return` - zwróć sumę zbiorów
    kluczy w obu słownikach.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: zbiór produktów, które należy kupić
    """
    return list1.keys() | list2.keys()
    pass


def products_only_on_one_list(list1: ShoppingList, list2: ShoppingList) -> int:
    """Zwróć liczbę produktów, które występują tylko na jednej z list zakupowych.

    W implementacji użyj wyłącznie instrukcji `return` - zwróć różnicę symetryczną
    zbiorów kluczy w obu słownikach.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: liczba produktów, które występują tylko na jednej z list zakupowych
    """
    return len(list1.keys() ^ list2.keys())
    pass


def two_dice_rolls_combinations() -> Dict[int, Set[Tuple[int, int]]]:
    """Zwróć słownik możliwych wyników rzutu dwiema kostkami.

    Przyjmij, że kostki są znaczone - zatem (1, 2) i (2, 1) to dwa różne wyniki.

    :return: słownik zawierający mapowanie sumy oczek na zbiór kombinacji
        wyników rzutu parą kostek
    """
    dice_rolls = {}
    all_rolls = []
    for first_die in range(1,7):
        for second_die in range(1,7):
            all_rolls.append((first_die, second_die))
    for roll_sum in range(2,13):
        dice_rolls[roll_sum] = {pair for pair in all_rolls if sum(pair) == roll_sum}
    return dice_rolls
    pass


def append_and_sort(lst: List[str]) -> List[str]:
    """Utwórz kopię listy wejściowej, dodaj do niej element 'abc', a na koniec
        zwróć jej elementy posortowane w porządku alfabetycznym (rosnącym).
    """
    new_lst = lst.copy()
    new_lst.append('abc')
    new_lst.sort()
    return new_lst
    pass