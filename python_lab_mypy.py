from typing import List
from typing import Tuple
from math import sqrt
from contracts import contract
# -*- coding: utf-8 -*-
""" Repaso interactivo de python
"""


@contract(lower='int,>0', upper='int,>0', returns=None)
def lower_up(lower: int, upper: int) -> None:
    """ 1: Returns a list of numbers from the lower number to the upper number:
    >>> lower_up(5,15)
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
        """
    for x in range(lower, upper+1):
        print(x)


@contract(args='tuple[N],N>0', kwargs='dict(str: (int))', returns=None)
def all_the_args(*args: str, **kwargs: str) -> None:
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args
    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print(args)
    print(kwargs)


@contract(tup='tuple[N],N>0', returns=None)
def may_20(tup: Tuple[int]) -> None:
    """ 3: Definir una tupla con 10 números.
    Imprimir la cantidad de números superiores a 20.
    >>> may_20((10, 16, 22, 26, 27, 30))
    22, 26, 27, 30
    """
    superiores = ""
    for x in tup:
        superiores = compara_20(superiores, x)

    print(superiores)


@contract(cad_temp='str', cadena='int,>0', returns='str')
def compara_20(cad_temp: str, cadena: int) -> str:
    """ Comparamos si es mayor a 20
    """
    if cadena > 20:
        cad_temp = concatena(cad_temp, cadena)
    return cad_temp


@contract(cad_temp='str', cadena='int,>0', returns='str')
def concatena(cad_temp: str, cadena: int) -> str:
    """ Concatenamos una cadena si esta o no vacia.
    """
    if cad_temp == "":
        cad_temp = str(cadena)
    else:
        cad_temp = cad_temp + ", " + str(cadena)
    return cad_temp


@contract(list_='list(str)', n='int,>0', returns='list(str)')
def word_filter(list_: List[str], n: int) -> List[str]:
    """ 4: Filtra las palabras que contienen más de n caracteres.
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'], 5)
    ['computer', 'software', 'python']
    """
    a = 1
    for i in range(len(list_)):
        list_ = word_list(list_, n, a, i)
        a = word_accepted(list_, n, a, i)
    return list_


@contract(li='list(str)', n='int,>0', a='int,>0', i='int', returns='list(str)')
def word_list(li: List[str], n: int, a: int, i: int) -> List[str]:
    if len(li[i-a]) <= n:
        li.remove(li[i-a])
    return li


@contract(list_='list(str)', n='int,>0', a='int,>0', i='int', returns='int')
def word_accepted(list_: List[str], n: int, a: int, i: int) -> int:
    if len(list_[i-a]) <= n:
        a = a + 1
    return a


@contract(list='str', returns='None')
def string_length(list: List[str]) -> None:
    """ 5: imprime el largo de una cadena de caracteres

    >>> string_length("popularity")
    10
    """
    print(len(list))


@contract(x='str', returns='None')
def is_vocal(x: str) -> None:
    """ 6: Determines if it is vocal

    >>> is_vocal('a')
    True
    >>> is_vocal('c')
    False
    """
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print(True)
    else:
        print(False)


@contract(year='int', returns=None)
def is_leap_year(year: int)-> None:
    """ 7: Determines if a year is a leap year.

    >>> is_leap_year(2016)
    True
    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(True)
    else:
        print(False)


@contract(word='str', returns='int')
def has_uppercase(word: str) -> int:
    """ 8: Evaluate if a word has uppercase letters

    >>> has_uppercase("MayuSculA")
    3
    """
    return sum(1 for i in word if i.isupper())


@contract(cadena='str', returns='int')
def contar_vocales(cadena: str) -> int:
    """ 9: Return number of vocales in a word.

    >>> contar_vocales('murcielago')
    5
    """
    suma = 0
    for x in cadena:
        suma += contar_vocales_2(x)

    return suma


def contar_vocales_2(x: str)-> int:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return 1
    else:
        return 0


@contract(list='list(int)', returns=None)
def square(list: List[int]) -> None:
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    temp = []
    for i in range(len(list)):
        temp.append(list[i]*list[i])

    print(temp)


@contract(n='int', returns='bool')
def is_prime(n: int)-> bool:
    """ 11:  Return if n is prime.

    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


@contract(n='int', returns='int')
def factorial(n: int) -> int:
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(int(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


@contract(n='int', returns='str')
def to_roman(n: int)-> str:
    """ 13: Convert number integer to Roman numeral

    >>> to_roman(598)
    '[DXCVIII]'
    """
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
           'V', 'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
    list.append(roman_num)
    return str(list).replace("'", "")


@contract(word1='str', word2='str', returns=None)
def rima(word1: str, word2: str) -> None:
    """ 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
    si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.

    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco
    >>> rima('azucar', 'barrer')
    no rima
    """
    if word1[len(word1)-1] == word2[len(word2)-1]:
        rima3(word1, word2)
    else:
        print('no rima')


def rima3(word1: str, word2: str) -> None:
    if word1[len(word1)-2] == word2[len(word2)-2]:
        rima2(word1, word2)
    else:
        print('no rima')


def rima2(word1: str, word2: str) -> None:
    if word1[len(word1)-3] == word2[len(word2)-3]:
        print('rima')
    else:
        print('rima un poco')


@contract(pesos='int', interes='float', anios='int', returns=None)
def capital(pesos: int, interes: float, anios: int) -> None:
    """ 15: Pide una cantidad de pesos, una tasa de interés y un numero de años.
    Muestra en cuanto se habrá convertido el capital inicial transcurridos esos
    años si cada año se aplica la tasa de interés introducida.

    >>> capital(10000, 4.5, 20)
    24117.14
    """
    resultado = pesos*(1 + interes/100) ** anios
    print(round(resultado, 2))
