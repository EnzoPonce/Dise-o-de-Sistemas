# Interfaz Reproductor
class Reproductor:
    def reproducir(self):
        pass

# Clase ReproductorMP3 (Incompatible con la interfaz Reproductor)
class ReproductorMP3:
    def __init__(self, archivo):
        self.archivo = archivo

    def reproducir_mp3(self):
        print(f"Reproduciendo archivo MP3: {self.archivo}")

# Clase ReproductorWAV (Incompatible con la interfaz Reproductor)
class ReproductorWAV:
    def __init__(self, archivo):
        self.archivo = archivo

    def reproducir_wav(self):
        print(f"Reproduciendo archivo WAV: {self.archivo}")

# Adaptador para ReproductorMP3
class AdaptadorMP3(Reproductor):
    def __init__(self, reproductor_mp3):
        self.reproductor_mp3 = reproductor_mp3

    def reproducir(self):
        self.reproductor_mp3.reproducir_mp3()

# Adaptador para ReproductorWAV
class AdaptadorWAV(Reproductor):
    def __init__(self, reproductor_wav):
        self.reproductor_wav = reproductor_wav

    def reproducir(self):
        self.reproductor_wav.reproducir_wav()

# Cliente
if __name__ == "__main__":
    reproductor_mp3 = ReproductorMP3("cancion.mp3")
    reproductor_wav = ReproductorWAV("sonido.wav")

    reproductor = Reproductor()

    adaptador_mp3 = AdaptadorMP3(reproductor_mp3)
    reproductor.reproducir()  # No se produce ninguna reproducción

    adaptador_wav = AdaptadorWAV(reproductor_wav)
    reproductor.reproducir()  # No se produce ninguna reproducción

    reproductor.reproducir()  # Reproducir el archivo WAV a través del adaptador WAV
    reproductor.reproducir()  # Reproducir el archivo MP3 a través del adaptador MP3

 