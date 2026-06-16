class Usuario:

    #Constructor
    def __init__(self, nombre, matricula, carrera, correo, activo):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera=carrera
        self.correo=correo
        self.activo=activo

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostrat_info(self):
        return f"ID:{self.id}, Nombre:{self.nombre}, Matricula:{self.matricula}, Carrera:{self.carrera.nombre_carrera}, Correo:{self.correo}, Activo: {self.activo}"
