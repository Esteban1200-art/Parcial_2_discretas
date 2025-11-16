#Solicitud de datos
#Solicitud datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita al usuario la longitud del lado del cuadrado.
    Retorna la longitud del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado
#Solicitud datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita al usuario la base y la altura del triángulo.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura
#Solicitud datos circulo
def solicitar_datos_circulo():
    """
    Solicita al usuario el radio del círculo.
    Retorna el radio como un número flotante.
    """
    radio = float(input("Ingrese el radio del círculo: "))
    return radio
def solicitar_datos_rectangulo():
    """
    Solicita al usuario la base y la altura del rectángulo.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return base, altura
def solicitar_datos_rombo():
    """
    Solicita al usuario las diagonales del rombo.
    Retorna las diagonales como números flotantes.
    """
    diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    return diagonal_mayor, diagonal_menor
def solicitar_datos_romboide():
    """
    Solicita al usuario la base y la altura del romboide.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del romboide: "))
    altura = float(input("Ingrese la altura del romboide: "))
    return base, altura
def solicitar_datos_trapecio():
    """
    Solicita al usuario las bases y la altura del trapecio.
    Retorna las bases y la altura como números flotantes.
    """
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    return base_mayor, base_menor, altura
def solicitar_datos_pentagono():
    """
    Solicita al usuario el perímetro y la apotema del pentágono.
    Retorna el perímetro y la apotema como números flotantes.
    Apotema se define como la distancia desde el centro del pentágono hasta el punto medio de uno de sus lados.
    """
    perimetro = float(input("Ingrese el perímetro del pentágono: "))
    apotema = float(input("Ingrese la apotema del pentágono: "))
    return perimetro, apotema


def mostrar_area_cuadrado(area):
    """
    Muestra el área del cuadrado al usuario.
    Parámetros:
        area (float): El área del cuadrado a mostrar.
    """
    print(f"El área del cuadrado es: {area}")
#Mostrar area triangulo
def mostrar_area_triangulo(area):    
    """
    Muestra el área del triángulo al usuario.
    Parámetros:
        area (float): El área del triángulo a mostrar.
    """
    print(f"El área del triángulo es: {area}")
#Mostrar area circulo
def mostrar_area_circulo(area):
    """
    Muestra el área del círculo al usuario.
    Parámetros:
        area (float): El área del círculo a mostrar.
    """
    print(f"El área del círculo es: {area}")
def mostrar_area_rectangulo(area):
    """
    Muestra el área del rectángulo al usuario.
    Parámetros:
        area (float): El área del rectángulo a mostrar.
    """
    print(f"El área del rectángulo es: {area}")
def mostrar_area_rombo(area):
    """
    Muestra el área del rombo al usuario.
    Parámetros:
        area (float): El área del rombo a mostrar.
    """
    print(f"El área del rombo es: {area}")
def mostrar_area_romboide(area):
    """
    Muestra el área del romboide al usuario.
    Parámetros:
        area (float): El área del romboide a mostrar.
    """
    print(f"El área del romboide es: {area}")
def mostrar_area_trapecio(area):
    """
    Muestra el área del trapecio al usuario.
    Parámetros:
        area (float): El área del trapecio a mostrar.
    """
    print(f"El área del trapecio es: {area}")
def mostrar_area_pentagono(area):
    """
    Muestra el área del pentágono al usuario.
    Parámetros:
        area (float): El área del pentágono a mostrar.
    """
    print(f"El área del pentágono es: {area}")


#Menu calculadora
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    Retorna la opción seleccionada por el usuario como un entero.
    """
    print("Calculadora de Áreas de Figuras Geométricas")
    print("1. Calcular área del cuadrado")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del círculo")
    print("4. Calcular área del rectángulo")
    print("5. Calcular área del rombo")
    print("6. Calcular área del romboide")
    print("7. Calcular área del trapecio")
    print("8. Calcular área del pentágono")
    print("9. Salir")
    opcion = int(input("Seleccione una opción (1-9): "))
    return opcion