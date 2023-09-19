#Alejandro Marin
#Daniel Buelvas

import tkinter as tk

numero = 0  # Variable para almacenar el resultado

def realizar_operacion():
    opcion = opcion_var.get()
    valor1 = float(valor1_entry.get())
    valor2 = float(valor2_entry.get())

    global numero  # Usamos la variable global "numero" para almacenar el resultado

    if opcion == "Suma":
        numero = valor1 + valor2
    elif opcion == "Resta":
        numero = valor1 - valor2
    elif opcion == "Multiplicación":
        numero = valor1 * valor2
    elif opcion == "División":
        if valor2 != 0:
            numero = valor1 / valor2
        else:
            numero = "Error: División por cero"
    elif opcion == "División Entera":
        if valor2 != 0:
            numero = valor1 // valor2
        else:
            numero = "Error: División por cero"
    elif opcion == "Exponente":
        numero = valor1 ** valor2
    elif opcion == "Módulo":
        if valor2 != 0:
            numero = valor1 % valor2
        else:
            numero = "Error: División por cero"
    else:
        numero = "Opción no válida"

    resultado_label.config(text="El resultado es: " + str(numero))

root = tk.Tk()
root.title("Calculadora")

opciones = ["Suma", "Resta", "Multiplicación", "División", "División Entera", "Exponente", "Módulo"]
opcion_var = tk.StringVar()
opcion_var.set(opciones[0])  # Establecer la opción predeterminada

valor1_entry = tk.Entry(root, width=10)
valor2_entry = tk.Entry(root, width=10)

menu_label = tk.Label(root, text="Operaciones disponibles:")
menu_label.pack()

menu_option = tk.OptionMenu(root, opcion_var, *opciones)
menu_option.pack()

valor1_label = tk.Label(root, text="Ingrese el primer valor:")
valor1_label.pack()
valor1_entry.pack()

valor2_label = tk.Label(root, text="Ingrese el segundo valor:")
valor2_label.pack()
valor2_entry.pack()

calcular_button = tk.Button(root, text="Calcular", command=realizar_operacion)
calcular_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()