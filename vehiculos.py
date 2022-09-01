class Vehiculo:
    def __init__(self, matricula, tipo, marca=None, modelo=None, color=None):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo = tipo

    def get_vehiculo(self, matricula):
        with open("C:/Users/Pipe/Documents/Python/transito/data/vehiculos.txt") as vehiculos:
            for vehiculo in vehiculos:
                data = vehiculo.split("|")
                if matricula == data[0]:
                    vehiculos.close()
                    return data

            else:
                vehiculos.close()
                return f"No se encontro el vehiculo con matricula {self.matricula}"


    def set_vehiculo(self):
        with open("C:/Users/Pipe/Documents/Python/transito/datavehiculos.txt") as vehiculos:
            vehiculos.write(f"{self.matricula}|{self.marca}|{self.modelo}\n")
            vehiculos.close()
            return True

    def arrancar(self, vel_final):
        return f"*** arrancando... *** hasta {vel_final}"

    def frenar(self):
        return "*** frenando... ***"
