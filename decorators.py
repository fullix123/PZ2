import time
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# 1. Декоратор замера времени
def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.info(f"[TIME] {func.__name__}: {end - start:.6f} сек")
        return result
    return wrapper


# 2. Декоратор логирования вызова
def call_logger(func):
    def wrapper(*args, **kwargs):
        logger.info(f"[CALL] Функция {func.__name__} вызвана")
        return func(*args, **kwargs)
    return wrapper


# 3. Декоратор проверки деления на ноль
def safe_division(func):
    def wrapper(x):
        if x == 0:
            raise ValueError("Деление на ноль запрещено")
        return func(x)
    return wrapper
