##1. Log execution time
##2. Memoization
##3. Test suite?

from shared.common import cls
from typing import Callable
import random
import time

cls()

class TimeTracker:
    def __init__(self) -> None:
        self.times = dict()

    def __call__(self, name:str):
        def decorator(func):
            def inner():
                start = time.time()
                func()
                self.times[name] = time.time() - start
            return inner
        return decorator

class UnaryMemo:
    def __init__(self, func) -> None:
        self.func = func
        self.cache = dict()

    def __call__(self, argument):
        if argument not in self.cache:
            self.cache[argument] = self.func(argument)
        return self.cache[argument]

tracker = TimeTracker()

@tracker('Fun')
def fun():
    time.sleep(1*random.random())

@UnaryMemo
def fun2(n:int) -> int:
    time.sleep(1)
    return n * 2

print(fun2(1))
print(fun2(1))
print(fun2(1))

#print(tracker.times)