from tkinter import *
from tkinter import messagebox
import random

ventana_juego = Tk()

ventana_juego.title("=yo=")

ventana_juego.geometry("700x700")

ventana_juego.resizable(0,0)

ventana_juego.config(bg="pink")

frame_1 = Frame(ventana_juego)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10, y=10)

titulo = Label(frame_1, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=250, y=10)

subtitulo1 = Label(frame_1, text="Especialidad en sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo1.place(x=300, y=50)

ventana_juego.mainloop()