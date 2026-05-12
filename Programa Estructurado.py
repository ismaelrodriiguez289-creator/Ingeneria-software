# Diccionario inicial de usuarios
usuarios = {
    "admin": "12345",
    "kenneth": "abcde"
}

# Función para solicitar datos
def solicitar_datos():
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")
    return usuario, contraseña


# Función para validar credenciales
def validar_credenciales(usuario, contraseña):
    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            return True
    return False


# Función para agregar un nuevo usuario
def agregar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    usuario = input("Nuevo usuario: ")

    if usuario in usuarios:
        print(" El usuario ya existe")
    else:
        contraseña = input("Nueva contraseña: ")
        usuarios[usuario] = contraseña
        print(" Usuario registrado correctamente")


# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario, contraseña = solicitar_datos()
            if validar_credenciales(usuario, contraseña):
                print(" Acceso concedido")
            else:
                print(" Acceso denegado")

        elif opcion == "2":
            agregar_usuario()

        elif opcion == "3":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida")


# Programa principal
if __name__ == "__main__":
    menu()
