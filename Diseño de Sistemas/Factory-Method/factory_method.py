from abc import ABC, abstractmethod


# Producto (Product) Interfaz
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass


# Productos Concretos (Concrete Products) Implementa la Interfaz Producto
class Perro(Animal):
    def hablar(self):
        return "Guau!"


class Gato(Animal):
    def hablar(self):
        return "Miau!"


class Leon(Animal):
    def hablar(self):
        return "Grrr!"


# Creador (Creator) Interfaz
class CreadorAnimales(ABC):
    @abstractmethod
    def crear_animal(self):
        pass


# Creador Concreto (Concrete Creator)
class CreadorDePerros(CreadorAnimales):
    def crear_animal(self):
        return Perro()


class CreadorDeGatos(CreadorAnimales):
    def crear_animal(self):
        return Gato()


class CreadorDeLeones(CreadorAnimales):
    def crear_animal(self):
        return Leon()


# Uso del Factory
def main():
    creador_perros = CreadorDePerros()
    animal = creador_perros.crear_animal()
    print(animal.hablar())  # Salida: "Guau!"

    creador_gatos = CreadorDeGatos()
    animal = creador_gatos.crear_animal()
    print(animal.hablar())  # Salida: "Miau!"


if __name__ == "__main__":
    main()

# En este ejemplo, Animal es la interfaz del producto, Perro y Gato son las clases concretas que implementan Animal.
# El CreadorAnimales es la interfaz del creador y CreadorDePerros y CreadorDeGatos son los creadores concretos que implementan el método crear_animal,
# instanciando los objetos concretos Perro y Gato, respectivamente.