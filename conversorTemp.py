import tkinter as tk
from tkinter import ttk
class Ventana:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion1=tk.IntVar()
        self.seleccion2=tk.IntVar()
        self.seleccion3=tk.IntVar()
        self.seleccion.set(2)
        #Introducir el dato
        self.label1=tk.Label(text="Cantidad:")
        self.label1.grid(column=0, row=0)
        
        self.dato=tk.StringVar()
        
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entry1.grid(column=1, row=0) 
       
        
        #Elegir en que grados queremos el resultado
        self.check1=tk.Checkbutton(self.ventana1,text="Kelvin", variable=self.seleccion1)
        self.check1.grid(column=0, row=4)
        self.check2=tk.Checkbutton(self.ventana1,text="Celsius", variable=self.seleccion2)
        self.check2.grid(column=1, row=4)
        self.check3=tk.Checkbutton(self.ventana1,text="Fahrenheit", variable=self.seleccion3)
        self.check3.grid(column=2, row=4)
         #Elegir la opcion que tenemos en grados
        self.radio1=tk.Radiobutton(self.ventana1,text="Kelvin", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.ventana1,text="Celsius", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.ventana1,text="Fahrenheit", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=1)
        self.boton2=ttk.Button(self.ventana1, text="Convertir a:")
        self.boton2.grid(column=1, row=3)
        self.boton2=ttk.Button(self.ventana1, text="Convertir a:",command=self.ConverirAKelvin)
        self.boton2.grid(column=1, row=3)
        #Lista de resultados
        self.label2=tk.Label(text="Celsius:")
        self.label2.grid(column=0, row=5)
        self.label3=tk.Label(text="Kelvin:")
        self.label3.grid(column=0, row=6)
        self.label4=tk.Label(text="Fahrenheit:")
        self.label4.grid(column=0, row=7)


        self.ventana1.mainloop()
    #Convertir a kelvin
    def ConverirAKelvin(self):
        valor1 = int(self.dato.get())
        valor = valor1 + 273
        self.label2.configure(text=valor)

vent = Ventana()