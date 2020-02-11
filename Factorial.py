# -*- coding: utf-8 -*-
#autor: Dex Loggica

from tkinter import *
import pymysql
from math import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext as st


class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora de Factorial")
        self.formulario()
    def formulario(self):
        self.labelframe1=ttk.LabelFrame(text="Factorial")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #NUMERO
        self.label1=ttk.Label(self.labelframe1, text="Ingresa un numero:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.numero=tk.IntVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.numero)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)
        #NUMERO
        self.label1=ttk.Label(self.labelframe1, text="Resultado:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        #Boton para calcular el factorial
        self.boton1=ttk.Button(self.labelframe1, text="Calcular",command=self.calcular_factorial)
        self.boton1.grid(column=0, row=2, padx=4, pady=4, columnspan=2)
        
    def calcular_factorial(self):
        numero=self.numero.get()
        factorial_total = 1
        while numero > 1:
            factorial_total *= numero
            numero -= 1
        print(factorial_total)
        return factorial_total
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

