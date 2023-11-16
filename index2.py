import tkinter as tk
import random

class SerpientesEscaleras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Serpientes y Escaleras")

        self.tablero = [[None] * 10 for _ in range(10)]
        self.posicion_jugador = 0
        self.jugador = None

        self.crear_tablero()
        self.boton_dado = tk.Button(self.ventana, text="Lanzar Dado", command=self.mover_jugador)
        self.boton_dado.grid(row=11, column=0, columnspan=10)

    def crear_tablero(self):
        for i in range(10):
            for j in range(10):
                color = "white"
                if (i == 0 and j == 0) or (i == 9 and j == 9):
                    color = "white"
                else:
                    color = random.choice(["blue", "red", "white"])

                celda = tk.Label(self.ventana, width=4, height=2, bg=color)
                celda.grid(row=i, column=j)
                self.tablero[i][j] = celda

        # Inicializar jugador
        self.jugador = tk.Canvas(self.ventana, width=20, height=20, bg="white", bd=0, highlightthickness=0)
        self.jugador.create_oval(5, 5, 15, 15, fill="green")
        self.jugador.grid(row=0, column=0)

    def mover_jugador(self):
        dado = random.randint(1, 6)
        print(f"Dado: {dado}")

        # Calcular nueva posición
        self.posicion_jugador += dado

        fila = self.posicion_jugador // 10
        columna = self.posicion_jugador % 10

        if self.posicion_jugador >= 99:
            print("¡Has ganado el juego!")
            self.boton_dado.config(state="disabled")
            return

        if fila < 10 and columna < 10:
            color_celda = self.tablero[fila][columna]['bg']
            if color_celda == "blue":
                self.posicion_jugador += 1
                print("¡Avanza una celda adicional por pisar una azul!")
            elif color_celda == "red":
                self.posicion_jugador -= 1
                print("¡Retrocede una celda por pisar una roja!")

            # Actualizar posición del jugador
            self.jugador.grid(row=fila, column=columna)

        print(f"Posición del jugador: {self.posicion_jugador}")

def main():
    ventana = tk.Tk()
    juego = SerpientesEscaleras(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
