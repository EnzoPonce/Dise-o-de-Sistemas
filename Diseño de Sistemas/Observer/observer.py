# Clase Observador (Observer)
class Observador:
    def actualizar(self, mensaje):
        pass

# Clase Sujeto (SujetoObservable)
class SujetoObservable:
    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        self._observadores.append(observador)

    def desuscribir(self, observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

# Clase Revista (SujetoObservable)
class Revista(SujetoObservable):
    def publicar_numero(self, numero):
        mensaje = f"¡Nuevo número de la revista publicado! Número: {numero}"
        self.notificar(mensaje)

# Clase Usuario (Observador)
class Usuario(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"¡{self.nombre} recibió una actualización!: {mensaje}")

if __name__ == "__main__":
    # Crear una revista
    revista = Revista()

    # Crear usuarios
    usuario1 = Usuario("Juan")
    usuario2 = Usuario("María")
    usuario3 = Usuario("Pedro")

    # Suscribir usuarios a la revista
    revista.suscribir(usuario1)
    revista.suscribir(usuario2)
    revista.suscribir(usuario3)

    # Publicar nuevos números de la revista
    revista.publicar_numero(1)
    revista.publicar_numero(2)

    # Desuscribir un usuario
    revista.desuscribir(usuario2)

    # Publicar otro número de la revista
    revista.publicar_numero(3)
