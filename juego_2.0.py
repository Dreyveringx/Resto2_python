import pygame
import time
import os

class JuegoAventura:
    def __init__(self):
        pygame.init()
        self.nombre_jugador = ""
        self.estado = "En curso"
        self.sonido_victoria = pygame.mixer.Sound("victoria.wav.mp3")
        self.sonido_derrota = pygame.mixer.Sound("punch-2-123106.mp3")

    def centrar_textos(self, textos):
        ancho_terminal = os.get_terminal_size().columns
        textos_centrados = []
        for texto in textos:
            espacio_en_blanco = (ancho_terminal - len(texto)) // 2
            texto_centrado = " " * espacio_en_blanco + texto + " " * espacio_en_blanco
            textos_centrados.append(texto_centrado)
        return textos_centrados

    def mostrar_texto_centrado(self, textos):
        textos_centrados = self.centrar_textos(textos)
        for texto in textos_centrados:
            print(texto)

    def iniciar_juego(self):
        while True:
            self.mostrar_texto_centrado(["\n", "Bienvenido", "\n", "◄[🏆]► En Busca del Tesoro ◄[🥇]►", "\n"])
            self.nombre_jugador = input("Ingrese nombre: ")
            self.comenzar_historia()
            if not self.reintentar_juego():
                break

    def comenzar_historia(self):
        print(f"\n 🌳Estamos en medio de una densa selva tropical, rodeados de vegetación exuberante y sonidos de animales desconocidos. ☀️ El sol se filtra a través de las hojas de los árboles, creando un ambiente misterioso🌲. ")
        print(f"\n\n 🤠{self.nombre_jugador}, eres un(a) intrépido explorador que ha estado buscando el legendario 🗿Tesoro de los Antiguos🗿  durante años. La leyenda cuenta que este tesoro está escondido en lo más profundo de esta selva y que otorgará inmensas riquezas y poder a quien lo encuentre. ")
        self.opcion_a()

    def opcion_a(self):
        print("\n\nte encuentras en un claro en medio de la selva. Frente a ti, hay un antiguo altar de piedra tallada con inscripciones en un idioma desconocido.\n\n ")
        decision = input("Tienes dos opciones: A Investigar el altar, B Ignorar el altar (A/B): ").upper()
        if decision == "A":
            self.opcion_a_izquierda()
        elif decision == "B":
            self.opcion_b()
        else:
            print("Opción no válida. Elige A o B.")
            self.opcion_a()

    def opcion_a_izquierda(self):
        print("\n\n➡️Al estudiar las inscripciones, descubres una serie de símbolos que te guían hacia una bifurcación en el camino. Las inscripciones sugieren que uno de los caminos lleva al tesoro, mientras que el otro es mortal\n\n")
        decision = input("¿Qué camino eliges, IZQUIERDA o DERECHA? (IZQUIERDA/DERECHA): ").upper()
        if decision == "IZQUIERDA":
            print("\n\n💢Sigues el camino de la izquierda y avanzas con cautela. Después de un tiempo, llegas a una trampa mortal y mueres.❌\n\n")
            self.estado = "Perdiste"
            self.mostrar_resultado()
        elif decision == "DERECHA":
            self.opcion_a_derecha()
        else:
            print("Opción no válida. Elige IZQUIERDA o DERECHA.")
            self.opcion_a_izquierda()

    def opcion_a_derecha(self):
        print("\n\n➡️El camino de la derecha te lleva a través de la selva densa, pero eventualmente llegas a una enorme puerta de piedra. Esta puerta parece ser la entrada a una antigua ciudad subterránea. Tu búsqueda continúa. \n\n Después de abrir la enorme puerta de piedra, entras en la antigua ciudad subterránea. Las paredes están adornadas con relieves de tesoros y riquezas. Parece que estás en el lugar correcto. \n\n  \n\n  Sin embargo, te enfrentas a un nuevo dilema:\n\n🧐EXPLORAR el interior de la ciudad subterranea. \n\n 🧐INVESTIGAR una puerta en la esquina que parece conducir a un pasaje oscuro.\n\n")
        decision = input("¿Cuál es tu decisión, EXPLORAR o INVESTIGAR? (EXPLORAR/INVESTIGAR): ").upper()
        if decision == "EXPLORAR":
            print("\n\n💢Una trampa antigua se activa, y una lluvia de dardos envenenados te alcanza. Tu búsqueda ha llegado a un final mortal.❌\n\n")
            self.estado = "Perdiste"
            self.mostrar_resultado()
        elif decision == "INVESTIGAR":
            print("\n\n🎸A medida que avanzas por el pasaje, llegas a una enorme cámara subterránea. En el centro de la cámara, brilla el Tesoro de los Antiguos.🎸\n\n")
            self.mostrar_texto_centrado(["\n",  "🏆  ¡𝒢𝒜𝒩𝒜𝒮𝒯𝐸!  🏆", "\n "])
            self.estado = "Ganaste"
            self.mostrar_resultado()
        else:
            print("Opción no válida. Elige EXPLORAR o INVESTIGAR.")
            self.opcion_a_derecha()

    def opcion_b(self):
        print(f"\n\n➡️Decides seguir adelante, ignorando el altar y confiando en tu instinto. Después de caminar un tiempo, llegas a un río. Tienes dos opciones: 🏊‍♂️ NADAR para cruzar el rio2. 🧐BUSCAR un camino alternativo siguiendo el rio.")
        decision = input("\n\nCuál es tu elección, NADAR o BUSCAR? (NADAR/BUSCAR): ").upper()
        if decision == "NADAR":
            print("\n\n💢🏊‍♂️Tratas de cruzar el río a nado, pero las fuertes corrientes te arrastran y mueres.❌\n\n")
            self.estado = "Perdiste"
            self.mostrar_resultado()
        elif decision == "BUSCAR":
            print("\n\nSigues el río y encuentras un puente colgante que te permite cruzar de manera segura. \n\n 💢Al otro lado eres sorprendido por una enorme pantera quien se abalanza contra ti y eres devorado en el acto.❌ \n\n")
            self.estado = "Perdiste"
            self.mostrar_resultado()
        else:
            print("Opción no válida. Elige NADAR o BUSCAR.")
            self.opcion_b()

    def reintentar_juego(self):
        reiniciar = input("\n\n¿Desea reiniciar el juego (SI) o salir del juego (NO)? (SI/NO): ").upper()
        return reiniciar == "SI"

    def mostrar_resultado(self):
        if self.estado == "Ganaste":
            print(f"{self.nombre_jugador}, ¡Felicidades! Has tenido éxito en tu búsqueda. El tesoro es tuyo.")
            self.sonido_victoria.play()
        else:
            self.mostrar_texto_centrado(["☠️¡PIERDES!☠️"])
            self.sonido_derrota.play()

        time.sleep(1)  
juego = JuegoAventura()
juego.iniciar_juego()
