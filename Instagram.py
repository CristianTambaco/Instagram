print("Instagram")

# Login Section
user = input("Usuario: ")
password = input("Contraseña: ")

if user == "Byron" and password == "123":
    print(f'Bienvenido {user}')
    print("Cargando tus publicaciones")
else:
    print("Lo sentimos, contraseña incorrecta")

# Sign-up Section
print("Regístrate para ver fotos y videos de tus amigos ")
facebook_login = input("Iniciar sesión con Facebook? (si/no): ").strip().lower()

if facebook_login == "si":
    print("Bienvenido")
else:
    mobile = input("Número de móvil o correo electrónico: ")
    full_name = input("Nombre completo: ")
    username = input("Nombre de usuario: ")
    new_password = input("Contraseña: ")
    print(f"Gracias por registrarte, {full_name}! Su cuenta ha sido creada.")

  