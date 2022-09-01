import automoviles


print("Bienvenido\n")

print("Seleccione el tipo de vehiculo")
print("1. Automovil\n2. Moto")
tipo_vehiculo = int(input("Tipo de vehiculo a consultar: "))


if tipo_vehiculo == 1:
    tipo = 'Automovil'
    matricula = input("Ingrese la matricula de su vehiculo: ")
    Automoviles = automoviles.Automoviles(matricula, tipo)
    datos_vehiculo = Automoviles.get_automovil(matricula, tipo)
    print(f"Matricula: {datos_vehiculo[0][0]}\nTipo de Vehiculo: {datos_vehiculo[1][1]}\nMarca: {datos_vehiculo[1][2]}\nModelo: {datos_vehiculo[1][3]}\nColor: {datos_vehiculo[1][4]}\nNuro de ruedas: {datos_vehiculo[0][1]}\nTraccion: {datos_vehiculo[0][2]}")


    

