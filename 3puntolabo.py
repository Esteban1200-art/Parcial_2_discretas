import random
#Generar la matriz
def generar_matriz(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
        
            fila.append(random.randint(20, 100))
        matriz.append(fila)
    return matriz

# recorre la matriz y detecta valores críticos
def detectar_criticos(matriz):
    criticos = []

    # For anidado para recorrer toda la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            if valor > 80:   # Temperatura crítica
                criticos.append((i, j, valor))
    
    return criticos


# Programa
print("=== Sistema de Monitoreo de Sensores ===")

# Tamaño de la matriz
n = int(input("Ingrese número de filas (sensores verticales): "))
m = int(input("Ingrese número de columnas (sensores horizontales): "))

# Generar la matriz de sensores
matriz_sensores = generar_matriz(n, m)

print("\nMatriz de sensores generada:")
for fila in matriz_sensores:
    print(fila)

# Detectar temperaturas peligrosas
criticos = detectar_criticos(matriz_sensores)

print("\nSensores en estado crítico (> 80°C):")

if len(criticos) == 0:
    print("No se encontraron sensores con temperatura crítica.")
else:
    for fila, col, valor in criticos:
        print(f"Sensor en posición ({fila}, {col}) con {valor}°C")
