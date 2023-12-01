import random
import time

from seleniumbase import BaseCase
from seleniumbase.undetected.webelement import WebElement


max_min = [
    (1, 3),
    (2, 4),
    (3, 5),
    (6, 10)
]


def rsleep(i, /):
    time.sleep(random.randint(*max_min[i]))


def cclick(self: BaseCase = None, args: tuple | list = None, kwargs: dict = None, sleep: int = None, func=None):
    e: WebElement = (func or self.wait_for_element_visible)(*(args or tuple()), **(kwargs or {}))

    if sleep:
        rsleep(sleep)

    e.uc_click()





