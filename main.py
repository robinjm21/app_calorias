import tkinter as tk 
from tkinter import messagebox
from datetime import date
from base_datos import registrar_sesion, obtener_historial
from calculadora import calcular_calorias
from graficos import graficar_historial
from base_datos import registrar_sesion, obtener_historial, verificar_logros
import random
from base_datos import conectar
import tkinter as tk
from tkinter import messagebox, Toplevel
from base_datos import verificar_logros
from win10toast import ToastNotifier

def guardar():
    try:
        peso = float(entry_peso.get())
        tiempo = float(entry_tiempo.get())
        met = float(entry_met.get())

        calorias = calcular_calorias(peso, tiempo, met)
        registrar_sesion(str(date.today()), peso, tiempo, met, calorias)

        nuevos = verificar_logros()
        if nuevos:
            for logro in nuevos:
                mostrar_notificacion("¡Logro desbloqueado!", f"Has alcanzado: {logro}")
        else:
            messagebox.showinfo("Sesión", f"Has quemado {calorias:.2f} calorías.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")


def reto_semanal():
    objetivo = random.choice([300, 500, 800, 1000])
    messagebox.showinfo(
        "Reto Semanal",
        f"Tu reto de esta semana: quema {objetivo} calorias.\n Completa para ganar una medalla!"
    )


def mostrar_logros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, logrado FROM logros")
    logros = cursor.fetchall()
    conn.close()

    ventana_logros = tk.Toplevel()
    ventana_logros.title("Logros")

    for l in logros:
        estado = "✅" if l[1] == 1 else "❌"
        tk.Label(ventana_logros, text=f"{estado} {l[0]}").pack()


def mostrar_grafico():
    graficar_historial()

def mostrar_notificacion(titulo, mensaje):
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry("300x120")
    ventana.configure(bg="#ffe599")

    tk.Label(ventana, text=mensaje, bg="#ffe599", wraplength=280, font=("Arial", 11)).pack(pady=15)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)

    ventana.after(7000, ventana.destroy)  # Cierra la notificación automáticamente tras 7s


def notificar_sistema(titulo, mensaje):
    notif = ToastNotifier()
    notif.show_toast(titulo, mensaje, duration=5, icon_path=None)


ventana = tk.Tk()
ventana.title("Contador de Calorias")

tk.Label(ventana, text="Peso (kg):").grid(row=0, column=0)
Tk_LabelTiempo = tk.Label(ventana, text="Tiempo (min):")
Tk_LabelTiempo.grid(row=1, column=0)
tk.Label(ventana, text="Nivel MET:").grid(row=2, column=0)

entry_peso = tk.Entry(ventana)
entry_tiempo = tk.Entry(ventana)
entry_met = tk.Entry(ventana)

entry_peso.grid(row=0, column=1)
entry_tiempo.grid(row=1, column=1)
entry_met.grid(row=2, column=1)

tk.Button(ventana, text="Guardar Sesion", command=guardar).grid(row=3, column=0, pady=5)
tk.Button(ventana, text="Ver Progreso", command=mostrar_grafico).grid(row=3, column=1, pady=5)
tk.Button(ventana, text="Reto Semanal", command=reto_semanal).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Ver Logros", command=mostrar_logros).grid(row=5, column=0, columnspan=2, pady=5)



ventana.mainloop()
