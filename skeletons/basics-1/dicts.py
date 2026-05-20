#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Słowniki
#
# -----------------------------------------------------------------------------

from typing import Dict, Any, List, Tuple, Optional, Set


def dict_intro() -> None:
    """Rozgrzewka: tworzenie i wypisywanie słownika.

    Utwórz w jednej instrukcji słownik {str -> int} zawierający następujące
    pary klucz-wartość: Adam=2, Bogdan=4, Cezary=1.
    Następnie wypisz całą zawartość słownika, po jednym wpisie w każdym wierszu.

    Przykładowo (kolejność wpisów może się różnić od poniższej):
      Adam = 2
      Bogdan = 4
      Cezary = 1

    (zob. "test" w pliku test/test_dict_intro.py)
    """
    dict = {
        "Adam" : 2,
        "Bogdan" : 4,
        "Cezary" : 1
    }
    for name in dict:
        print(f"{name} = {dict[name]}")
    return None
    pass


# Alias `Menu` na typ `Dict[str, float]` poprawia czytelność kodu
# oraz upraszcza wprowadzanie ewentualnych zmian w programie.
Menu = Dict[str, float]


def update_price(menu: Menu, dish: str) -> None:
    """Zwiększ wartość skojarzoną z kluczem `dish` w słowniku `menu` o 50.

    :param menu: menu, które należy zaktualizować
    :param dish: danie, którego cena powinna zostać zmieniona
    """
    menu[dish] += 50
    pass


def fix_key(dct: Dict[str, Any], incorrect_key: str, correct_key: str) -> Dict[str, Any]:
    """Skoryguj ewentualny błędny klucz w słowniku.

    Utwórz kopię słownika wejściowego `dct` i jeśli słownik ten zawiera błędy
    klucz `incorrect_key`, wówczas przepisz (w kopii) jego wartość do nowego
    ("poprawnego") klucza `correct_key` oraz usuń błędny klucz.

    W implementacji nie twórz nowego słownika "od zera", tylko skorzystaj
      z funkcjonalności kopiowania wbudowanej w język Python!

    :param dct: słownik, który (potencjalnie) należy skorygować
    :param incorrect_key: błędny klucz (do poprawy)
    :param correct_key: poprawny klucz, który powinien zastąpić błędny klucz
    :return: poprawny słownik (KOPIA słownika wejściowego z poprawionym kluczem)
    """
    new_dct = dct.copy()
    for key in dct:
        if key == incorrect_key:
            new_dct[correct_key] = new_dct.pop(incorrect_key)
    return new_dct
    pass


def update_all_prices(menu: Menu) -> None:
    """Zwiększ każdą z wartości w słowniku `menu` o 50.

    :param menu: menu, które należy zaktualizować
    """
    for dish in menu:
        menu[dish] += 50
    return None
    pass


# TODO: Zdefiniuj alias `ClassRegister` na typ umożliwiający przechowywanie
#   informacji o ocenach poszczególnych uczniów, tj. mapowanie nazwy
#   ucznia na listę ocen (będących liczbami zmiennoprzecinkowymi).
ClassRegister = Dict[str, list[float]]


def average_grades_1(register: ClassRegister) -> Dict[str, float]:
    """Oblicz średnią dla każdego ucznia.

    Przyjmij, że każdy uczeń ma co najmniej jedną ocenę.

    :param register: dziennik ocen
    :return: mapowanie nazwy ucznia na średnią jego ocen
    """
    class_mean = {}
    for student in register:
        grades = register[student]
        class_mean[student] = sum(grades) / len(grades)
    return class_mean
    pass


# [OPT]
def average_grades_2(register: ClassRegister) -> Dict[str, Optional[float]]:
    """Oblicz średnią dla każdego ucznia.

    Jeśli uczeń nie posiada ani jednej oceny, przyjmij że średnia wynosi None.

    :param register: dziennik ocen
    :return: mapowanie nazwy ucznia na średnią jego ocen (albo None, jeśli
        dany uczeń nie posiada ocen)
    """
    class_mean = {}
    for student in register:
        grades = register[student]
        if len(grades) == 0:
            class_mean[student] = None
            continue
        class_mean[student] = sum(grades) / len(grades)
    return class_mean
    pass


def letters_frequencies(s: str) -> Dict[str, int]:
    """Zwróć zestawienie częstości występowania poszczególnych liter w danym słowie.

    :param s: łańcuch znaków, dla którego obliczana jest częstość wystąpień liter
    :return: mapowanie litery na częstość jej występowania
    """
    freq_map = {}
    for letter in set(s):
        how_many = 0
        for i in s:
            if i == letter:
                how_many += 1
        freq_map[letter] = how_many
    return freq_map
    pass


def letters_frequency_2(s: str) -> Tuple[Dict[str, int], int]:
    """Zwróć zestawienie częstości występowania poszczególnych liter w danym słowie
    ORAZ liczbę unikalnych liter.

    W implemnetacji wywołaj funkcję `letters_frequencies()`.

    :param s: łańcuch znaków, dla którego obliczane są statystyki
    :return: 2-elementowa krotka złożona ze słownika częstości występowania
        poszczególnych liter oraz z liczby unikalnych liter
    """
    return (letters_frequencies(s), len(set(s)))    
    pass


def census(register: Dict[str, Dict[str, Any]]) -> Tuple[Dict[str, int], float]:
    """Wyznacz liczbę osób z poszczególnych państw oraz średni wiek wszystkich osób.

    Przyjmij, że rejestr zawiera dane choć jednej osoby oraz że informacje
    w słowniku są poprawne (nie ma brakujących kluczy itd.).

    :param register: spis osób w formacie {N: {'address': {'country': C}, 'age': A}
        gdzie N - nazwa osoby; C - państwo, z którego osoba pochodzi; A - wiek osoby
    :return: 2-elementowa krotka złożona ze słownika opisującego liczbę osób
        z poszczególnych państw oraz ze średniego wieku wszystkich osób
    """
    number_of_citizens = {}
    age_sum = 0

    for name in register:
        person = register[name]
        country = person["address"]["country"]
        age = person["age"]

        if country not in number_of_citizens:
            number_of_citizens[country] = 0
        
        number_of_citizens[country] += 1
        age_sum += age
    
    avg_age = age_sum / len(register)
    
    return (number_of_citizens, avg_age)
    pass


# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def sum_shopping_lists(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    """Scal dwie listy zakupowe w jedną.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: scalone listy zakupowe
    """
    for item in list2:
        if item in list1:
            list1[item] += list2[item]
            continue
        list1[item] = list2[item]
    return list1
    pass


def sum_shopping_lists_nonempty(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    """Scal dwie listy zakupowe w jedną, z pominięciem produktów o krotności 0.

    W implementacji wywołaj funkcję `sum_shopping_lists()`.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: scalone listy zakupowe
    """
    list_sum = sum_shopping_lists(list1, list2)
    for item in list(list_sum):
        if list_sum[item] == 0:
            del list_sum[item]
    return list_sum
    pass


def filter_pesels_by_name_initial(persons: Dict[str, str], name_initial: str) -> Set[str]:
    """Zwróć zbiór PESEL-i osób, których imię zaczyna się zadaną literę.

    Implementacja powinna zawierać wyłącznie instrukcję `return`.
    W rozwiązaniu użyj set comprehension.

    :param persons: baza osób {PESEL -> osoba}
    :param name_initial: inicjał imienia użyty do filtrowania
    :return: zbiór PESEL-i osób
    """
    return {pesel for pesel in persons if persons[pesel][0] == name_initial}
    pass
