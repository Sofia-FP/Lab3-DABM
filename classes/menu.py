
class menu:
    def __init__(self,Temp):
        self.Temp = Temp
    
    def ver(self):
        print("Bienvenido al sistema".center(20,"*"))
        print("1. Toma de datos")
        print("2. Configuración de parámetros")
        print("3. Reportes")
        print("4. Salir")
        op = input(">>> ")
        return op
       
class MenuTomaDatos:
    
     def ver(self):
        print("Menú Toam de Datos".center(20,"*"))
        print("1. Definir cantidad de datos por rango")
        print("2. Definir cantidad de datos por gráfica")
        op = input(">>> ")

        return op

class MenuReportes:
    def ver(self):
        print("Menú Reportes".center(20,"*"))
        print("1. Gráfica de datos")
        print("2. Valores máximo y mínimo")
        print("3. Promedio")
        print("4. salir")
        op = input(">>> ")

        return op

if __name__=='__main__':
    m = menu("xxx")
    m.ver()