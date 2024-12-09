import tkinter as tk

#Agrega el numero o simbolo en la entrada de texto
def agregar_numero(numero):
    entrada.insert(tk.END, numero)

#Evalua la expresion matematica ingresada y muestra el resultado. En caso de existir un error muestra el str "Error"
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def limpiar():
    entrada.delete(0, tk.END)

#Crea la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

#Crea la entrada para ingresar los numeros
entrada = tk.Entry(ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

#Creacion de los botones de la calculadora
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

#Agregar los botones a la ventana

fila = 1
columna = 0
for boton in botones:
    if boton == "C":
        tk.Button(ventana, text=boton, width=5, height=2, command=limpiar).grid(row=fila, column=columna)
    elif boton == "=":
        tk.Button(ventana, text=boton, width=5, height=2, command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, width=5, height=2, command=lambda b=boton: agregar_numero(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

#Inicia el bucle en la Ventana
ventana.mainloop()