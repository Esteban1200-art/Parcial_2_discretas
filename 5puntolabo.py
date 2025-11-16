# ------------------------------------------
# Clase CuentaBancaria
# ------------------------------------------
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"[{self.titular}] Depósito exitoso (+{monto}). Nuevo saldo: {self.saldo}")
        else:
            print("Error: el monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print("Error: el monto debe ser positivo.")
        elif monto > self.saldo:
            print(f"[{self.titular}] Fondos insuficientes. Saldo disponible: {self.saldo}")
        else:
            self.saldo -= monto
            print(f"[{self.titular}] Retiro exitoso (-{monto}). Nuevo saldo: {self.saldo}")

    def consultar_saldo(self):
        print(f"[{self.titular}] Saldo actual: {self.saldo}")


# ------------------------------------------
# PROGRAMA PRINCIPAL (INTERACTIVO)
# ------------------------------------------
print("=== SISTEMA BANCARIO ===")

# El usuario crea su propia cuenta
nombre = input("Ingrese su nombre para crear una cuenta: ")
cuenta_usuario = CuentaBancaria(nombre)

print(f"\nCuenta creada correctamente para {nombre}.\n")

# Menú de opciones
while True:
    print("Seleccione una operación:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        cuenta_usuario.depositar(monto)

    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta_usuario.retirar(monto)

    elif opcion == "3":
        cuenta_usuario.consultar_saldo()

    elif opcion == "4":
        print("\nGracias por usar el sistema bancario.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

    print("")  # Salto visual
