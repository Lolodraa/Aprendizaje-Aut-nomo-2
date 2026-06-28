import random
import tkinter as tk
from tkinter import messagebox

# Variables
minus = "abcdefghijklmnñopqrstuvwxyz"
capital = minus.upper()
number = "1234567890"
characters = "#$%&/()=?¡*¨[]_:;.,}{<>?"

def generar_contraseña():
    entrada = caja_longitud.get()

    if not entrada.isdigit():
        messagebox.showerror("Error", "Debe ingresar solo números.")
        return

    longitud = int(entrada)

    if longitud < 10:
        messagebox.showwarning("Nivel bajo", "Mínimo 10 caracteres.")
        return

    # Nivel medio o alto
    if 10 <= longitud < 20:
        respuesta = messagebox.askyesno("Nivel medio","El nivel de la contraseña es inseguro. ¿Desea cambiar a ALTO (20+)?")

        if respuesta:
            longitud = 20


    # Generación segura
    contraseña = [
        random.choice(capital),
        random.choice(minus),
        random.choice(number),
        random.choice(characters)
    ]

    todos = capital + minus + number + characters

    i = 4
    while i < longitud:
        contraseña.append(random.choice(todos))
        i += 1

    random.shuffle(contraseña)

    contraseña_final = ""
    for c in contraseña:
        contraseña_final += c

    # Evaluación
    tiene_mayus = any(c in capital for c in contraseña_final)
    tiene_num = any(c in number for c in contraseña_final)
    tiene_sim = any(c in characters for c in contraseña_final)

    es_valida = tiene_mayus and tiene_num and tiene_sim

    if longitud >= 20 and es_valida:
        nivel = "ALTO"
    elif longitud >= 10 and es_valida:
        nivel = "MEDIO"

    resultado.set(f"Contraseña:\n{contraseña_final}\n\nNivel: {nivel}")

# VENTANA
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x300")

tk.Label(ventana, text="GENERADOR SEGURO", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(ventana, text="Longitud de la contraseña:").pack()
tk.Label(ventana, text="(Longitud minima de 10)").pack()

caja_longitud = tk.Entry(ventana)
caja_longitud.pack(pady=5)

tk.Button(
    ventana,
    text="Generar contraseña",
    command=generar_contraseña
).pack(pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Consolas", 10)).pack(pady=10)

ventana.mainloop()
