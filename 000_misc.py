from typing import Callable

#Función de orden superior: Recibe una función y retorna None.
def f1(func:Callable):
    func()

#Función de orden superior: Sin parámetros y retorna una función.
def f2():
    def result() -> Callable:
        pass
    return result

#Función de orden superior: Recibe una función y retorna una función.
def f3(func:Callable) -> Callable:
    return func

#Función generada con metaprogramación.
data = "def m1():\n\tprint('Función generada con metaprogramación')"
exec(data)
#m1()

