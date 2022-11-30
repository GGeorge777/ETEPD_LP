class Animal():
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def set_nome(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def locomove(self):
        pass

class Aquatico(Animal):

     def locomove(self):
        print("Um animal aquatico nada.")


class Terrestre(Animal):
     def locomove(self):
        print("animal terrestre anda.")

