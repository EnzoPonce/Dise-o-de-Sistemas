# Clase Pizza: El producto final que queremos construir
class Pizza:
    def __init__(self):
        self.tipo = None
        self.tamano = None
        self.masa = None
        self.ingredientes = []

    def __str__(self):
        return f"\nTipo: {self.tipo}\nTamaño: {self.tamano}\nMasa: {self.masa}\nIngredientes: {', '.join(self.ingredientes)}"

# Constructor abstracto (Builder)
class PizzaBuilder:
    def set_tipo(self, tipo):
        self.pizza.tipo = tipo
        return self

    def set_tamano(self, tamano):
        self.pizza.tamano = tamano
        return self

    def set_masa(self, masa):
        self.pizza.masa = masa
        return self

    def agregar_ingrediente(self, ingrediente):
        self.pizza.ingredientes.append(ingrediente)
        return self

    def build(self):
        return self.pizza

# Constructor concreto PizzaBuilderVegetariana
class PizzaBuilderVegetariana(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        return self.pizza

# Constructor concreto PizzaBuilderEspecial
class PizzaBuilderEspecial(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        return self.pizza

# Director
class DirectorPizza:
    def __init__(self, builder):
        self.builder = builder

    def construir_pizza(self, tipo, tamano, masa, ingredientes):
        return self.builder.set_tipo(tipo) \
                           .set_tamano(tamano) \
                           .set_masa(masa) \
                           .agregar_ingrediente(ingredientes[0]) \
                           .agregar_ingrediente(ingredientes[1]) \
                           .agregar_ingrediente(ingredientes[2]) \
                           .build()

# Cliente que utiliza los constructores concretos junto con el director para construir pizzas personalizadas
if __name__ == "__main__":
    director = DirectorPizza(PizzaBuilderVegetariana())
    pizza_vegetariana = director.construir_pizza("Vegetariana", "Grande", "Tradicional", ["Queso", "Ananá", "Aceitunas"])
    print("Pizza Vegetariana:")
    print(pizza_vegetariana)

    director = DirectorPizza(PizzaBuilderEspecial())
    pizza_especial = director.construir_pizza("Especial", "Mediana", "Delgada", ["Queso", "Jamón", "Aceitunas"])
    print("\nPizza Especial:")
    print(pizza_especial)