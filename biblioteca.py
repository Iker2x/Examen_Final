# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario, cuenta):  
        self.__nombre = nombre  # Encapsulamiento
        self.__id_usuario = id_usuario
        self.__cuenta = cuenta

    def buscar_autor(self, autor):
        print(f"Usuario: {self.__nombre}, se encuentra buscando libros del autor: {autor}")

    def actualizar_cuenta(self):
        print(f"Actualizando la cuenta del usuario {self.__nombre}.")

# Clase Catálogo
class Catalogo:
    def __init__(self):  
        self.__libros = []  # Lista privada de libros

    def buscar_autor(self, autor):
        print(f"Buscando en el catálogo libros del autor: {autor}")

    def actualizar_catalogo(self):
        print("Actualizando el catálogo.")

# Clase LibrosDisponibles
class LibrosDisponibles:
    def __init__(self): 
        self.__lista_libros = []  # Lista privada de libros disponibles

    def consultar_disponibilidad(self):
        print("Consultando disponibilidad de libros.")

# Clase Préstamo
class Prestamo:
    def __init__(self, id_prestamo, fecha_inicio, fecha_termino, penalidades=0):  
        self.__id_prestamo = id_prestamo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino 
        self.__penalidades = penalidades

    def realizar_prestamo(self):
        print(f"Realizando el préstamo del libro con el ID: {self.__id_prestamo}")

    def verificar_penalidades(self):
        if self.__penalidades > 0:
            print(f"El préstamo tiene penalidades: ${self.__penalidades}")
        else:
            print("No hay penalidades.")

# Clase base Persona (Herencia)
class Persona:
    def __init__(self, nombre, id_persona):  
        self.__nombre = nombre
        self.__id_persona = id_persona

    def saludar(self):
        print(f"Hola, soy {self.__nombre}")

# Clase UsuarioPremium heredando de Persona (Ejemplo de Herencia y Polimorfismo)
class UsuarioPremium(Persona):
    def __init__(self, nombre, id_persona, beneficios): 
        super().__init__(nombre, id_persona)
        self.beneficios = beneficios

    def mostrar_beneficios(self):
        print(f"Beneficios de Usuario Premium: {self.beneficios}")

# Programa principal
def main():
    try:
        # Crear instancias
        usuario = Usuario("Juan Pérez", 123, "Cuenta123")
        catalogo = Catalogo()
        libros_disponibles = LibrosDisponibles()
        prestamo = Prestamo(1, "2024-12-01", "2024-12-15")

        # Operaciones
        usuario.buscar_autor("Gabriel García Márquez")
        catalogo.buscar_autor("Miguel de Cervantes")
        catalogo.actualizar_catalogo()
        libros_disponibles.consultar_disponibilidad()
        prestamo.realizar_prestamo()
        prestamo.verificar_penalidades()

        # Polimorfismo y herencia
        usuario_premium = UsuarioPremium("Ana López", 456, "Descuentos y préstamos ilimitados")
        usuario_premium.saludar()
        usuario_premium.mostrar_beneficios()

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Punto de entrada
if __name__ == "__main__":  
    main()
