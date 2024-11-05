from shared.common import cls as clear_screen
from atexit import register

#@staticmethod y @classmethod

clear_screen()

class Example:
    def max(cls, a, b):
        print(cls.__name__)
        return a if a > b else b

#print(Example.max(1, 2))
#print(Example.max is Example.max)
#print(Example().max is Example().max)

#register

#@register
#def on_finish():
#    print('Programa completado con exito')

