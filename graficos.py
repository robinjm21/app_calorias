import matplotlib.pyplot as plt
from base_datos import obtener_historial

def graficar_historial():
    datos = obtener_historial()
    if not datos:
        print("No hay regristros aun.")
        return

    fechas = [d[0] for d in datos]
    calorias = [d[1] for d in datos]

    plt.plot(fechas, calorias, marker="o")
    plt.title("Progreso de Calorias Quemadas")
    plt.xlabel("Fecha")
    plt.ylabel("Calorias")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()