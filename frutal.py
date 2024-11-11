from abc import ABC, abstractmethod


class Frutal(ABC):
    def __init__(self, fruto, derivado):
        self.fruto = fruto
        self.__derivado = derivado
        pass

    @property
    def derivado(self):
        return self.__derivado
    
    @derivado.setter
    def derivado(self, producto):
        self.__derivado = producto

    @abstractmethod
    def riego():
        pass
    
    @abstractmethod
    def floracion():
        pass

    @abstractmethod
    def cosecha():
        pass

    @abstractmethod
    def poda():
        pass

    def __str__(self):
        return f'{self.fruto}'
    