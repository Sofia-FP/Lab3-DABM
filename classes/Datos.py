import matplotlib.animation as animation
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime
from .Parametros import *
import pandas as pd
import statistics
import serial
import csv


global puerto
puerto = serial.Serial('COM4',9600)
global pausa
pausa = False
global tempT

class Datos:
    file = "C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv"
    def __init__(self,nombre,temperatura,fecha,hora):
        self.nombre = nombre
        self.temperatura = temperatura
        self.referencia = fecha
        self.referencia = hora
        
    def verDatos(self):
        header = ["NOMBRE","TEMPERATURA","FECHA","HORA"]
        datos = [[self.nombre,self.temperatura,self.fecha,self.hora]]
        print(tabulate(datos, header, tablefmt="grid"))

    def save(self):
        f = open(self.file,'a')
        linea = ";".join([self.nombre,self.temperatura,self.Fecha])
        f.write(linea+"\n")
        f.close()

def DatosRango():
    print('Registrar nuevo paciente')
    nombre = input("Nombre: ")
    now = datetime.now()
    fecha = now.strftime("%m/%d/%Y")
    hora = now.strftime("%H:%M:%S")
    len = input('Cantidad de datos que desea tomar: ')
    len = int(len)
    tempT = []
    for i in range(len):
        temperatura = puerto.readline().decode().strip()
        tempT.append(temperatura)
        datos = Datos(nombre,temperatura,fecha,hora)
        f = open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv","a")
        f.write(";".join([nombre,temperatura,fecha,hora])+"\n")
    #print(tempT)
    return tempT


def DatosGrafica():
    try:
        puerto.close()
        puerto.open()
    except:
        print('Problemas abriendo puerto')
    
    def onclick(event):
        global pausa
        print('Pausa')
        pausa = True
    
    fig, ax = plt.subplots()
    ydata = []
    
    def update_data(i):
        if not pausa:
            punto = puerto.readline().decode().strip()
            ydata.append(punto)
            ax.clear()
            ax.plot(ydata)
    
    ani = animation.FuncAnimation(fig,update_data)
    fig.canvas.mpl_connect('button_press_event',onclick)
    plt.show()

def Parametros():
    hipotermia = input(int('Ingrese a partir de que valor considera que el paciente tiene hipotermia'))
    normal = input(int('Ingrese a partir de que valor considera que el paciente tiene temperatura normal'))
    hipertermia = input(int('Ingrese a partir de que valor considera que el paciente tiene fiebre'))
    a = open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv","w")
    a.writelines(hipotermia,normal,hipertermia)
    a.close()


def getAllDatos():
    a = open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv","r")
    datos = a.readlines()
    return datos

def Grafica():
    f= open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv")
    reader = csv.reader(f,delimiter=';')
    datos = []
    for row in reader:
        datos.append(int(row[1]))
    plt.title('Datos temperatura')
    plt.plot(datos, color='red')
    plt.show()

def MaxMin():
    f= open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv")
    reader = csv.reader(f,delimiter=';')
    datos = []
    fecha = []
    hora = []
    for row in reader:
        datos.append(int(row[1]))
        fecha.append(row[2])
        hora.append(row[3])
    Max = datos.index(max(datos))
    Min = datos.index(min(datos))
    print('Los datos de la temperatura máxima registrada son: ',max(datos),'° ',fecha[Max],hora[Max])
    print('Los datos de la temperatura mínima registrada son: ',min(datos),'° ',fecha[Min],hora[Min])


def Promedio():
    f= open("C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Datos.csv")
    reader = csv.reader(f,delimiter=';')
    datos = []
    for row in reader:
        datos.append(int(row[1]))
    print('El promedio de temperaturas registradas es de',statistics.mean(datos))
