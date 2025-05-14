class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.reservas = []

    def hacer_reserva(self, sala, fecha, hora_inicio, hora_fin):
        reserva = Reserva(fecha, hora_inicio, hora_fin, self, sala)
        self.reservas.append(reserva)
        sala.reservas.append(reserva)
        return reserva


class Sala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.reservas = []


class Reserva:
    def __init__(self, fecha, hora_inicio, hora_fin, usuario, sala):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.usuario = usuario
        self.sala = sala

    def mostrar_info(self):
        return (f"Reserva de {self.usuario.nombre} en sala {self.sala.nombre} "
                f"el {self.fecha} de {self.hora_inicio} a {self.hora_fin}")


if __name__ == "__main__":
    usuario = Usuario("Ana", "ana@email.com")
    sala = Sala("Sala 101", 25)

    reserva = usuario.hacer_reserva(sala, "2025-05-20", "10:00", "12:00")
    print(reserva.mostrar_info())
