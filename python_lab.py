# -*- coding: utf-8 -*-
def lower_up(lower, upper):
    """ 1: Returns a list of numbers from the lower number to the upper number:
    >>> lower_up(5, 15)
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
        
def all_the_args(*args, **kwargs):
    """ 2: Return an array. Use * to expand positional
    args and use ** to expand keyword args
    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    [['a', 3], ['b', 4]]
    """
    lists = []
    print(args)
    for key, value in sorted(kwargs.items()):
        temp = [key, value]
        lists.append(temp)
    print(lists)

def may_20(*tup):
    """ 3: Definir una tupla con 10 números.
    Imprimir la cantidad de números superiores a 20.
    >>> may_20(10, 16, 22, 26, 27, 30)
    22, 26, 27, 30
    """
    lists = []
    for x in tup:
        lists.append(may_20_2(x))
    y = str(list(filter(None, lists)))
    print(y[1:-1])

def may_20_2(x):
    if x > 20:
        return x

def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen más de n caracteres.
    >>> word_filter(['hello','bye', 'computer', 'software', 'python'], 5)
    ['computer', 'software', 'python']
    """
    lists = []
    for item in list_of_words:
        word_filter_2(item, lists, n)
    print(lists)

def word_filter_2(item, lists, n):
    if len(item) > n:
        lists.append(item)

def string_length(list):
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    print(len(list)
          
def is_vocal(x):
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
          
def is_leap_year(year):
    """ 7: Determines if a year is a leap year.
    >>> is_leap_year(2016)
    True
    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(True)
    else:
        print(False)
          
def has_uppercase(word):
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase("MayuSculA")
    3
    """
    print(sum(1 for i in word if i.isupper()))


          
          
def contar_vocales(cadena):
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    print(sum(1 for c in cadena if c in ('a', 'e', 'i', 'o', 'u')))


def square(list):
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    print([i ** 2 for i in list])


def is_prime(n):
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n > 1:
        loopprime(n)
    else:
        print(False)


def prime(n, i):
    if (n % i) == 0:
        print(False)
        return
    else:
        print(True)
        return


def loopprime(n):
    for i in range(2, n):
        prime(n, i)
        break


def factorial(n):
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1L, 2L, 6L, 24L, 120L]
    >>> factorial(30)
    265252859812191058636308480000000L
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def to_roman(num):
    """ 13: Convert number integer to Roman numeral
        >>> to_roman(598)
        ['DXCVIII']
    """
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
           'V', 'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(num / val[i])
        roman_num += syb[i] * count
        num -= val[i] * count
    list.append(roman_num)
    return list


def rima(word1, word2):
    """ 14: Indica si dos palabrar riman. Si coinciden
        las 3 ultimas letras rima,
        si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco.
    >>> rima('azucar', 'barrer')
    no rima
    """
    if word1[len(word1)-1] == word2[len(word2)-1]:
        rima3(word1, word2)
    else:
        print('no rima')


def rima3(word1, word2):
    if word1[len(word1)-2] == word2[len(word2)-2]:
        rima2(word1, word2)
    else:
        print('no rima')


def rima2(word1, word2):
    if word1[len(word1)-3] == word2[len(word2)-3]:
        print('rima')
    else:
        print('rima un poco.')


def capital(pesos, interes, anios):
    """ 15: Pide una cantidad de pesos, una tasa de interés y un
        numero de años. Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada año se aplica
    la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
    24117.14
    """
    resultado = pesos * (1 + interes / 100) ** anios
    print(round(resultado, 2))
