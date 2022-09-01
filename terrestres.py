import vehiculos

Vehiculos = vehiculos.Vehiculo

class Terrestres(Vehiculos):
    def __init__(self, matricula, tipo, marca=None, modelo=None, color=None, , nro_ruedas=None, traccion=None):
        super().__init__(matricula, tipo, marca, modelo, color)
        self.nro_ruedas = nro_ruedas
        self.traccion = traccion


    def get_vehiculo(self, matricula):
        with open("C:/Users/Pipe/Documents/Python/transito/data/terrestres.txt") as terrestres:
            for vehiculo in terrestres:
                data = vehiculo.split("|")
                if matricula == data[0] and data[1]:
                    My_vehiculo = Vehiculos
                    vehiculos.close()
                    return data

            else:
                vehiculos.close()
                return f"No se encontro el vehiculo con matricula {self.matricula}"