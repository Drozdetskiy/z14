'''
Ex1
Это простое упражнение на использование упаковок.
Определите функцию print_given, которая для каждого переданного аргумента
будет распечатывать на отдельной строке через пробел имя аргумента
(если таковое имеется),
значение аргумента, тип аргумента.

Аргументы без имени должны быть распечатаны раньше именованных.
Порядок печати аргументов без имени важен: он должен совпадать с порядком,
в котором аргументы передаются. Порядок печати аргументов с именем неважен.

Пример:
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1)
>>> 1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
[1, 2, 3] <class 'list'>
one <class 'str'>
two <class 'str'>
three <class 'str'>
one 1 <class 'int'>
two 2 <class 'int'>

print_given()
'''
from functools import wraps


def print_given(*args, **kwargs):
    for item in args:
        print(item, type(item))
    for key, value in kwargs.items():
        print(key, value, type(value))



'''
Ex2
Написать функцию sort_by_abc,
на вход которой подаётся некоторое количество (не больше сотни)
разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).

Функция должна вернуть список в порядке лексикографического возрастания
названий этих чисел в английском языке.

Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2,
поскольку слово two в словаре встречается позже слова three,
а слово three -- позже слова one (иначе говоря, поскольку
выражение 'one' < 'three' < 'two' является истинным)

Пример:
Sample Input:
[0, 1, 1, 2, 3, 5, 8, 13]
Sample Output:
[8, 5, 1, 1, 13, 3, 2, 0]

Использовать
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
'''


def sort_by_abc(_list):
    number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return sorted(_list, key=lambda x: number_names[x])

'''
Ex3
Напишите функцию composition(f, g), которая принимает на вход две
функции: f и g, -- и возвращает их композицию.

Не вдаваясь в лишние сейчас детали,  назовём композицией 𝑓∘𝑔 двух
заданных функций 𝑓, 𝑔 функцию ℎ, для которой

  ℎ(𝑥)=𝑓(𝑔(𝑥))

Определите функцию композиции, предполагая, что аргументы
у функции g могут быть какие угодно,
и любое возвращаемое функцией g значение будет
корректным аргументом для функции f.

Примеры:
h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))

>>> 36


h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))

>>> 36


h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))

>>> 6592
'''


def composition(func_1, func_2):
    # return lambda *args, **kwargs: func_1(func_2(*args, **kwargs))
    def new_func(*args, **kwargs):
        return func_1(func_2(*args, **kwargs))
    return new_func


'''
Ex4
Напишите декоратор flip, который делает так, что задекорированная функция
принимает все свои неименованные аргументы в порядке, обратном тому,
в котором их передали (для аргументов с именем не вполне правильно
учитывать порядок, в котором они были переданы)

Пример:
@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)
>>> 2.0
'''


def flip(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return new_func

'''
Ex5
Напишите декоратор introduce_on_debug, который
делает так, что задекорированная функция печатает своё имя
при вызове, но только если переменная debug имеет значение True.

Пример:
@introduce_on_debug(debug=False)
def identity(x):
    return x

identity(239)
>>> 239

@introduce_on_debug(debug=True)
def identity(x):
    return x

identity(57)
>>> identity
57
'''


def introduce_on_debug(debug):
    def _inner(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            if debug:
                print(func.__name__)
            return func(*args, **kwargs)
        return new_func
    return _inner

