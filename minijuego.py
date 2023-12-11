import random
import os
import platform

# Definición de la clase Jugador para representar a los jugadores en el juego
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos = 0

# Definición de la clase JuegoAzar para manejar la lógica del juego
class JuegoAzar:
    def __init__(self):
        self.mi_numero = None
        self.numero_contrincante = None
        self.nombre_jugador = None

    # Inicia el juego generando números aleatorios para el jugador y el contrincante
    def iniciar_juego(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.mi_numero = random.randint(1, 10)
        self.numero_contrincante = random.randint(1, 10)
        return self.jugar()

    # Maneja la lógica del juego, donde el jugador intenta adivinar el número del contrincante
    def jugar(self, menu):  # Añade el parámetro menu
        intentos = 0
        while True:
            self.limpiar_pantalla()
            print(f"Intentos: {intentos}")
            intento = int(input("Adivina el número de tu contrincante: "))
            intentos += 1

            if intento == self.numero_contrincante:
                print(f"¡Felicidades, {self.nombre_jugador}! Adivinaste el número en {intentos} intentos.")
                menu.actualizar_ranking(self.nombre_jugador, intentos)  # Actualiza el ranking al finalizar el juego
                return intentos
            elif intento < self.numero_contrincante:
                print("El número de tu contrincante es mayor. ¡Sigue intentando!")
            else:
                print("El número de tu contrincante es menor. ¡Sigue intentando!")

    # Limpia la pantalla de la consola según el sistema operativo
    def limpiar_pantalla(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

# Definición de la clase Menu para gestionar las opciones del juego
class Menu:
    def __init__(self):
        self.jugadores = []
        self.ranking_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'ranking.txt')

    # Muestra las opciones del menú
    def mostrar_menu(self):
        print("1. Jugar")
        print("2. Ranking")
        print("3. Salir")

    # Inicia un nuevo juego y actualiza el ranking
    def jugar(self):
        nombre_jugador = input("Ingresa tu nombre de jugador: ")
        juego = JuegoAzar()
        intentos = juego.iniciar_juego(nombre_jugador)
        juego.jugar(self)  # Pasa la instancia del menú al juego

    # Muestra el ranking de jugadores
    def mostrar_ranking(self):
        if not self.jugadores:
            print("Aún no hay jugadores en el ranking.")
            return

        print("Ranking:")
        for jugador in sorted(self.jugadores, key=lambda x: x.intentos):
            nombre = jugador.nombre
            intentos_totales = jugador.intentos
            print(f"{nombre}: Intentos totales = {intentos_totales}")

    # Actualiza el ranking, considerando si el jugador ya está presente y si ha mejorado su puntuación
    def actualizar_ranking(self, nombre_jugador, intentos):
        for jugador in self.jugadores:
            if jugador.nombre == nombre_jugador:
                # Si el jugador ya está en el ranking, actualiza la puntuación si es mejor
                if intentos < jugador.intentos:
                    jugador.intentos = intentos
                break
        else:
            # Si el jugador no está en el ranking, agrégalo con su puntuación
            nuevo_jugador = Jugador(nombre_jugador)
            nuevo_jugador.intentos = intentos
            self.jugadores.append(nuevo_jugador)

        self.guardar_ranking()

    # Carga el ranking desde el archivo si existe, o lo crea si no existe
    def cargar_ranking(self):
        if not os.path.exists(self.ranking_file_path):
            # Si el archivo no existe, créalo con contenido vacío
            with open(self.ranking_file_path, 'w') as file:
                pass

        try:
            with open(self.ranking_file_path, 'r') as file:
                # Lee las líneas del archivo y crea instancias de Jugador
                lines = file.readlines()
                for line in lines:
                    nombre, intentos = line.strip().split(': ')
                    jugador = Jugador(nombre)
                    jugador.intentos = int(intentos)
                    self.jugadores.append(jugador)
        except ValueError as e:
            print(f"Error al cargar el ranking: {e}")

    # Guarda el ranking en el archivo
    def guardar_ranking(self):
        try:
            with open(self.ranking_file_path, 'w') as file:
                for jugador in self.jugadores:
                    file.write(f"{jugador.nombre}: {jugador.intentos}\n")
        except IOError as e:
            print(f"Error al guardar el ranking: {e}")

    def salir(self):
        print("Saliendo del programa")
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

# Instancia y ejecución del menú
menu = Menu()
menu.ejecutar_menu()
