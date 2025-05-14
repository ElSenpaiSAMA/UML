class Vehiculo:
    def __init__(self, marca):
        self.marca = marca


class Coche(Vehiculo):
    def __init__(self, marca, modelo, motor):
        super().__init__(marca)
        self.modelo = modelo
        self.motor = motor

    def mostrar_info(self):
        return f"Coche {self.marca} {self.modelo}, Motor: {self.motor.tipo}"


class Camion(Vehiculo):
    def __init__(self, marca, capacidad_carga):
        super().__init__(marca)
        self.capacidad_carga = capacidad_carga

    def mostrar_info(self):
        return f"Camión {self.marca}, Carga: {self.capacidad_carga} kg"


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo


if __name__ == "__main__":
    motor1 = Motor("Gasolina")
    coche1 = Coche("Toyota", "Corolla", motor1)
    camion1 = Camion("Volvo", 8000)

    print(coche1.mostrar_info())
    print(camion1.mostrar_info())
