import math
from decorators import time_logger, call_logger, safe_division


@time_logger
@call_logger
def linear(x):
    return x


@time_logger
@call_logger
def square(x):
    return x ** 2


@time_logger
@call_logger
def cube(x):
    return x ** 3


@time_logger
@call_logger
@safe_division
def inverse(x):
    return 1 / x


@time_logger
@call_logger
def sine(x):
    return math.sin(x)


# Словарь функций для удобного выбора
FUNCTIONS = {
    "1": ("y = x", linear),
    "2": ("y = x^2", square),
    "3": ("y = x^3", cube),
    "4": ("y = 1/x", inverse),
    "5": ("y = sin(x)", sine),
}
