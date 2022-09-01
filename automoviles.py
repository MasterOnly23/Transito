# import vehiculos
import terrestres

# Vehiculo= vehiculos.Vehiculo
Terrestres = terrestres.Terrestres


class Automoviles(Terrestres):

    def __init__(self, matricula, tipo_automovil, color, traccion, cilindraje, torque):
        # Vehiculo.__init__(matricula, marca, modelo)
        # Terrestres.__init__(nro_ruedas)
        self.matricula = matricula
        self.tipo_automovil = tipo_automovil
        self.color = color
        self.traccion = traccion
        self.cilindraje = cilindraje
        self. torque = torque

    def get_automovil(self, matricula):
        with open("ruta archivo automoviles.txt", "r") as automoviles:
            for auto in automoviles:
                data = auto.split('|')
                if  matricula == data[0]:
                    automoviles.close()
                    Myvehiculo = Vehiculo()
                    Portierra = Terrestres()
                    data_vehiculo = Myvehiculo.get_vehiculo(data[0])
                    data_vehiculo_terrestre = Portierra.get_terrestre(data[0])
                    return data + data_vehiculo + data_vehiculo_terrestre
            
            else:
                automoviles.close()
                return False


    def set_autimovil(self):
        with open("ruta archivo automoviles.txt", "a") as automoviles:
            automoviles.write(f"{self.matricula}|{self.tipo_automovil}|{self.color}|{self.traccion}|{self.cilindraje}|{self.torque}\n")
            automoviles.close()
            return True