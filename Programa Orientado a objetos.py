class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        # Encapsulamiento
        self.__nombre_usuario = nombre_usuario
        self.__contraseña = contraseña

    def validar_acceso(self, usuario, contraseña):
        return (
            self.__nombre_usuario == usuario
            and self.__contraseña == contraseña
        )

    def obtener_nombre(self):
        return self.__nombre_usuario


class SistemaAcceso:
    def __init__(self):
        self.usuarios = []

    # Agregar usuario
    def agregar_usuario(self, nombre, contraseña):
        # Verificar si ya existe
        for u in self.usuarios:
            if u.obtener_nombre() == nombre:
                print(" El usuario ya existe")
                return

        nuevo = Usuario(nombre, contraseña)
        self.usuarios.append(nuevo)
        print(" Usuario registrado correctamente")

    # Solicitar datos
    def solicitar_datos(self):
        usuario = input("Ingrese usuario: ")
        contraseña = input("Ingrese contraseña: ")
        return usuario, contraseña

    # Validar credenciales
    def validar_credenciales(self, usuario, contraseña):
        for u in self.usuarios:
            if u.validar_acceso(usuario, contraseña):
                return True
        return False

    # Menú del sistema
    def menu(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Iniciar sesión")
            print("2. Registrar usuario")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuario, contraseña = self.solicitar_datos()
                if self.validar_credenciales(usuario, contraseña):
                    print(" Acceso concedido")
                else:
                    print(" Acceso denegado")

            elif opcion == "2":
                print("\n--- Registro ---")
                nombre = input("Nuevo usuario: ")
                contraseña = input("Nueva contraseña: ")
                self.agregar_usuario(nombre, contraseña)

            elif opcion == "3":
                print(" Saliendo del sistema...")
                break

            else:
                print(" Opción inválida")


# Programa principal
if __name__ == "__main__":
    sistema = SistemaAcceso()

    # Usuarios iniciales
    sistema.agregar_usuario("admin", "1234")
    sistema.agregar_usuario("kenneth", "abcd")

    sistema.menu()
