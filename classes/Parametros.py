
class Temperatura():
    def __init__(self,HipoMin,HipoMax,NormalMin,NormalMax,HiperMin,HiperMax):
        self.HipoMin=float(HipoMin)
        self.HipoMax=float(HipoMax)
        self.NormalMin=float(NormalMin)
        self.NormalMax=float(NormalMax)
        self.HiperMin=float(HiperMin)
        self.HiperMax=float(HiperMax)
        self._file = "C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Parametros.csv"

    def Save(self):
        file = open(self._file,"a")
        datos = str(self.HipoMin) +";"+str(self.HipoMax)+";"+str(self.NormalMin)+";"+str(self.NormalMax)+";"+str(self.HiperMin)+";"+str(self.HiperMax)+"\n"
        file.write(datos)
        file.close()
  
    def Cambiar(self):
        file = open(self._file,"w")
        datos = str(self.HipoMin) +";"+str(self.HipoMax)+";"+str(self.NormalMin)+";"+str(self.NormalMax)+";"+str(self.HiperMin)+";"+str(self.HiperMax)+"\n"
        file.write(datos)
        file.close()
        Load()
        

def Load():
    rangos = []
    try:
        fileR = "C:/Users/anaso/Documents/Visual Studio/DABM/Lab3/database/Parametros.csv"
        f = open(fileR,"r")
        datos = f.readlines()
        f.close()
        for d in datos:
            datos = d.replace("\n","")
            datos = d.split(";")
            HipoMin=datos[0]
            HipoMax=datos[1]
            NormalMin=datos[2]
            NormalMax=datos[3]
            HiperMin=datos[4]
            HiperMax=datos[5]
            t = Temperatura(HipoMin,HipoMax,NormalMin,NormalMax,HiperMin,HiperMax)
            rangos.append(t)
            print(rangos)
        return rangos
    except:
        print("No se han determinado parametros")