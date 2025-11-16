contador_ingresos = 0

print("=== SISTEMA DE PROCESAMIENTO DE LOGS ===")

usuario_sistema = input("Ingrese su nombre de usuario para acceder: ").strip()

if usuario_sistema == "":
    print("Error: Debe ingresar un nombre válido.")
    exit()

contador_ingresos += 1
print(f"\nBienvenido, {usuario_sistema}.")
print(f"Ingresos al sistema: {contador_ingresos}\n")

logs = [
    ("ana", "08:00", "09:00"),
    ("juan", "09:10", "10:00"),
    ("ana", "10:15", "11:00"),
    ("maria", "11:05", "12:00"),
    ("juan", "13:00", "14:00")
]

procesados = []
i = 0

while i < len(logs):
    procesados.append(logs[i])
    i += 1


usuarios = {}           # contará accesos
detalles_usuario = []   # guardará horas del usuario logueado

for registro in procesados:
    usuario, entrada, salida = registro

    # contar accesos
    if usuario in usuarios:
        usuarios[usuario] += 1
    else:
        usuarios[usuario] = 1

    # guardar horas del usuario logueado
    if usuario == usuario_sistema:
        detalles_usuario.append((entrada, salida))

print(f"RESULTADOS DEL USUARIO: {usuario_sistema}")

if usuario_sistema in usuarios:
    print(f"Total de accesos en logs: {usuarios[usuario_sistema]}\n")
    print("Detalles de cada acceso:\n")

    for entrada, salida in detalles_usuario:
        print(f"Usuario: {usuario_sistema} | Entrada: {entrada} | Salida: {salida}")
else:
    print("El usuario no aparece en los logs registrados.")

print(f"\nIngresos al sistema en esta ejecución: {contador_ingresos}")
