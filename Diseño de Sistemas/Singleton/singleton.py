class Singleton(object):
    __instance = None  # atributo privado tipo clase

    #Definimos el metodo new ya que se ejecuta antes del init 
    def __new__(cls, val):  #constructor privado para crear y devolver una instancia del objeto
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


if __name__ == '__main__': 
    #Se crea una lista, un bucle y una nueva instancia de la clase Singleton, pasando el valor de str(i) como argumento.
    #Dado que es un Singleton, solo se creará una instancia en la primera iteración del bucle.
    Loggs = []
    for i in range(5):
        Loggs.append(Singleton(str(i))) 
        print("Objeto: ", Loggs[i], "Numero de log: ", Loggs[i].val)
