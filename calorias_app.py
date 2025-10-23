# Calorias_app.py
import csv
from datetime import date 

class Session:
    def __init__(self, fecha, peso, tiempo, met):
        self.fecha = fecha
        self.peso = peso
        self.tiempo = tiempo
        self.met = met

    def calcular_calorias(self):
        return self.met * self.peso * (self.tiempo / 60)

    def guarda_sesion(sesion):
        with open('historial.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sesion.fecha, sesion.peso, sesion.tiempo, sesion.met, sesion.calcular_calorias()])

    def mostrar_historial():
        try:
            with open('historial.csv', 'r') as file:
                reader = csv.reader(file)
                print("Fecha | Peso | Tiempo(min) | MET | Calorias")
                for row in reader:
                    print(' | '.join(row))
        except FileNotFoundError:
            print('No hay historial todavia')


    def main():
        print("=== APP CONTADOR DE CALORIAS ===")
        peso = float(input("Ingresa tu peso (Kg): "))
        tiempo = float(input("Tiempo carriendo (minutos): "))
        met = float(input("Nivel de esfuerzo (MET): "))

        sesion = sesion(str(date.today()), peso, tiempo, met)
        calorias = sesion.calcular_calorias()

        print(f"Has quemado aprodimadamente {calorias:.2f} caliras hoy.")

        Session.guarda_sesion(sesion)
        Session.mostrar_historial()
      

    if __name__ == "__main__":
        main()