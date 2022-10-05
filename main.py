from classes.Datos import *
from classes.menu import *

def main():
    Menu = menu("Datos Temperatura")
    op = Menu.ver()
    if op == "1":
        Menu2 = MenuTomaDatos()
        op2 = Menu2.ver()
        if op2 == '1':
            DatosRango()
            #visualizacion()
            main()
        elif op2 == '2':
            DatosGrafica()
            #visualizacion()
            main()
        elif op2 == '3':
            quit()
        else:
            print('Opción inválida')
            print(" ")
            main()
    elif op == '2':
        Parametros()
        main()
    elif op == '3':
        Menu2 = MenuReportes()
        op2 = Menu2.ver()
        if op2 == "1":
            Grafica()
            main()
        elif op2 == "2":
            MaxMin()
            main()
        elif op2 == "3":
            Promedio()
            main()
        elif op2 == "4":
            quit()
        else:
            print('Opción inválida')
            print(" ")
            main()
    elif op == '4':
        quit()
    else:
        print('Opción inválida')
        

if __name__=='__main__':
   
    main()