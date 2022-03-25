import tkinter as tk
class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.label = tk.Label(self.ventana,text="1")
        self.label.pack()
        self.boton1 = tk.Button(self.ventana,text="Incrementear",command = self.incrementar)
        self.boton2 = tk.Button(self.ventana,text="Decrementar",command = self.decrementar)
        self.boton1.pack()
        self.boton2.pack()
        self.valor = 1
        self.ventana.mainloop()
    
    def incrementar(self):
        self.valor +=1 
        self.label.config(text=self.valor)

    def decrementar(self):
        self.valor -=1
        if self.valor<2:
            self.label.configure(foreground = "red")
        else:
            self.label.configure(foreground = "blue")
        self.label.config(text=self.valor)

ventana1 = Ventana()
