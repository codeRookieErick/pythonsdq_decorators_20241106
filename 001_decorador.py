from typing import Any, Callable

from shared.common import cls
cls()

#def log_execution(func:Callable[[], None]) -> Callable[[], None]:
#    def result() -> None:
#        print('Se ha llamado la función')
#        func()
#    return result

#Metodo magico
#class LogExecution:
#    def __init__(self, func:Callable[[], None]) -> None:
#        self.func = func
#
#    def __call__(self):
#        print('Se ha llamado la función por LogExecution')
#        self.func()

#La sintaxis:
# @A
# def B():
#   pass
# 1. Evalua 'def B(): pass'
# 2. Evalua 'A'
# 3. Reemplaza B con el resultado de eval('A')(eval('def B(): pass'))
#ejemplo = eval('log_execution')(eval('ejemplo'))

#'Estrategia' factory
#def log(text:str):
#    def decorator(func:Callable[[], None]) -> Callable[[], None]:
#        def result() -> None:
#            print(text)
#            func()
#        return result
#    return decorator

#class Log:
#    def __init__(self, text:str) -> None:
#        self.text = text
#    
#    def __call__(self, func:Callable[[], None]) -> Callable[[], None]:
#        def inner():
#            print(self.text)
#            func()
#        return inner

#class LogBuilder:
#    def __init__(self) -> None:
#        self.originals = []
#
#    def get_original(self, index:int):
#        return self.originals[index]
#
#    def __call__(self, text:str):
#        def decorator(func:Callable[[], None]) -> Callable[[], None]:
#            self.originals.append(func)
#            def inner():
#                print(text)
#                func()
#            return inner
#        return decorator

#logBuilder = LogBuilder()

def ejemplo() -> None:
    print('Función ejemplo')

#ejemplo = log_execution(ejemplo)

ejemplo()