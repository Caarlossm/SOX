import random
import os
import platform

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos = 0

class JuegoAzar:
    def __init__(self):
        self.mi_numero = None
        self.numero_contrincante = None
        self.nombre_jugador = None

    def iniciar_juego(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.mi_numero = random.randint(1, 10)
        self.numero_contrincante = random.randint(1, 10)
        return self.jugar()

    def jugar(self):
        intentos = 0
        while True:
            self.limpiar_pantalla()
            print(f"Intentos realizados: {intentos}")
            intento = int(input("Adivina el número de tu contrincante: "))
            intentos += 1

            if intento == self.numero_contrincante:
                print(f"¡Felicidades, {self.nombre_jugador}! Has adivinado el número en {intentos} intentos.")
                return intentos
            elif intento < self.numero_contrincante:
                print("El número de tu contrincante es mayor. ¡Sigue intentando!")
            else:
                print("El número de tu contrincante es menor. ¡Sigue intentando!")

    def limpiar_pantalla(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

class Menu:
    def __init__(self):
        self.jugadores = []
        self.ranking_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'rankingpuntuacion.txt')

    def mostrar_menu(self):
        print("\n==== Menú ====")
        print("1. Jugar")
        print("2. Ver Ranking")
        print("3. Salir")

    def jugar(self):
        nombre_jugador = input("Ingresa tu nombre de jugador: ")
        juego = JuegoAzar()
        intentos = juego.iniciar_juego(nombre_jugador)
        self.actualizar_ranking(nombre_jugador, intentos)

    def mostrar_ranking(self):
        if not self.jugadores:
            print("Aún no hay jugadores en el ranking.")
            return

        print("\n==== Ranking ====")
        for jugador in sorted(self.jugadores, key=lambda x: x.intentos):
            nombre = jugador.nombre
            intentos_totales = jugador.intentos
            print(f"{nombre}: Intentos totales = {intentos_totales}")

    def actualizar_ranking(self, nombre_jugador, intentos):
        for jugador in self.jugadores:
            if jugador.nombre == nombre_jugador:
                if intentos < jugador.intentos:
                    jugador.intentos = intentos
                break
        else:
            nuevo_jugador = Jugador(nombre_jugador)
            nuevo_jugador.intentos = intentos
            self.jugadores.append(nuevo_jugador)

        self.guardar_ranking()

    def cargar_ranking(self):
        if not os.path.exists(self.ranking_file_path):
            with open(self.ranking_file_path, 'w') as file:
                pass

        with open(self.ranking_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                nombre, intentos = line.strip().split(': ')
                jugador = Jugador(nombre)
                jugador.intentos = int(intentos)
                self.jugadores.append(jugador)

    def guardar_ranking(self):
        with open(self.ranking_file_path, 'w') as file:
            for jugador in self.jugadores:
                file.write(f"{jugador.nombre}: {jugador.intentos}\n")

    def salir(self):
        print("¡Gracias por jugar! Saliendo del programa.")
        exit()

    def ejecutar_menu(self):
        self.cargar_ranking()
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-3): ")

            if opcion == '1':
                self.jugar()
            elif opcion == '2':
                self.mostrar_ranking()
            elif opcion == '3':
                self.salir()

menu = Menu()
menu.ejecutar_menu()
