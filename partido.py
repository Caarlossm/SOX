import random
import time  

class Partido:
    def __init__(self, E1, ocasiones, E2):
        self.equipo1 = E1
        self.ocasiones = ocasiones
        self.equipo2 = E2
        self.velocidad = 0
        self.resultado = None

    def iniciar_partido(self):
        print(f"¡Comienza el partido entre {self.equipo1} y {self.equipo2}!")
        time.sleep(2) 

    def anotar_gol(self, equipo):
        print(f"¡Gol para {equipo}! ¡Gran jugada!")
        time.sleep(2) 
        self.ocasiones += 1

    def cambiar_velocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad
        print(f"La velocidad del partido ha cambiado a {nueva_velocidad}.")
        time.sleep(2) 

    def simular_ocasion(self):
        if random.random() < 0.5:
            equipo_que_anota = random.choice([self.equipo1, self.equipo2])
            self.anotar_gol(equipo_que_anota)
        else:
            print("¡Oportunidad perdida! No hay gol esta vez.")
            time.sleep(2)

    def simular_partido(self):
        self.iniciar_partido()

        for _ in range(self.ocasiones):
            self.simular_ocasion()

        if self.ocasiones % 2 == 0:
            self.resultado = f"¡El partido termina en empate {self.ocasiones}-{self.ocasiones}!"
        elif self.ocasiones % 2 == 1:
            ganador = random.choice([self.equipo1, self.equipo2])
            self.resultado = f"¡{ganador} gana el partido {self.ocasiones}-{self.ocasiones - 1}!"

        print(f"¡Fin del partido! {self.resultado}")


partido_ejemplo = Partido("EquipoA", 5, "EquipoB")
partido_ejemplo.simular_partido()
