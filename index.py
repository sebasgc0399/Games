import tkinter as tk
import unittest

class SudokuApp:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Juego de Sudoku")

        self.tablero = [[0]*9 for _ in range(9)]
        self.entradas = {}

        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        for i in range(9):
            for j in range(9):
                entrada = tk.Entry(self.ventana, 
                                   width=2, 
                                   font=('Arial', 18), 
                                   justify='center')
                entrada.grid(row=i, column=j)
                self.entradas[(i, j)] = entrada

        boton_validar = tk.Button(self.ventana, 
                                  text="Validar Tablero", 
                                  command=self.validar_tablero)
        boton_validar.grid(row=10, 
                           column=0, 
                           columnspan=9)

    def validar_tablero(self):
        valido = True
        for i in range(9):
            for j in range(9):
                valor = self.entradas[(i, j)].get()
                if not valor.isdigit() or not 0 < int(valor) <= 9:
                    valido = False
                    break

        if valido:
            print("Tablero válido")
        else:
            print("Tablero inválido")

def main():
    ventana = tk.Tk()
    SudokuApp(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
