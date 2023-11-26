import random
import time

from seleniumbase import SB
from seleniumbase.fixtures.base_case import BaseCase
from seleniumbase.undetected.webelement import WebElement

max_min = [
    (1, 3),
    (2, 4),
    (3, 5),
    (6, 10)
]

sb: BaseCase | None = None


def execute(code: str):
    global sb

    with SB(uc=True) as sb:
        exec(code, locals(), globals())


def rsleep(i, /):
    time.sleep(random.randint(*max_min[i]))


def cclick(*args, kwargs: dict = None, sleep: int = None, func=None):
    e: WebElement = (func or sb.wait_for_element_visible)(*args, **(kwargs or {}))

    if sleep:
        rsleep(sleep)

    e.uc_click()





