import math
def validar(*valores):
    for v in valores:
        # Si viene como string directamente (letras o cadenas)
        if isinstance(v, str):
            # Intentar convertirlo a número por si es "5" o "3.2"
            try:
                v_num = float(v)
            except:
                raise ValueError("No se permiten letras, solo números positivos.")
        else:
            v_num = v

        # Ahora verificar si es realmente un número
        try:
            v_num = float(v_num)
        except:
            raise ValueError("El valor ingresado no es un número válido.")

        # Revisar si es negativo
        if v_num < 0:
            raise ValueError("No se permiten números negativos.")
def area_cuadrado(lado):
    try:
        validar(lado)
        """Calcula el área de un cuadrado dado el lado.
           Retorna el área calculada del cuadrado.
             Parámetros:
                  lado (float): La longitud del lado del cuadrado.
                  area = lado * lado
                  return area
        """
        area = lado * lado
        return area
    except Exception as e:
        return f"Error en área_cuadrado: {e}"

#Area Triangulo
def area_triangulo(base, altura):
    try:
        validar(base, altura)
        """Calcula el área de un triángulo dado la base y la altura.
           Retorna el área calculada del triángulo.
             Parámetros:
                  base (float): La longitud de la base del triángulo.
                  altura (float): La altura del triángulo.
                  area = (base * altura) / 2
                  return area
        """
        area = (base * altura) / 2
        return area
    except Exception as e:
        return f"Error en área_triangulo: {e}"

#Area circulo
def area_circulo(radio):
    try:
        validar(radio)
        """Calcula el área de un círculo dado el radio.
           Retorna el área calculada del círculo.
             Parámetros:
                  radio (float): La longitud del radio del círculo.
                  area = pi * radio * radio
                  return area
        """
        area = math.pi * (radio ** 2)
        return area
    except Exception as e:
        return f"Error en área_circulo: {e}"

def area_rectangulo(base, altura):
    try:
        validar(base, altura)
        """Calcula el área de un rectángulo dado la base y la altura.
           Retorna el área calculada del rectángulo.
             Parámetros:
                  base (float): La longitud de la base del rectángulo.
                  altura (float): La altura del rectángulo.
                  area = base * altura
                    return area
        """
        area = base * altura
        return area
    except Exception as e:
        return f"Error en área_rectangulo: {e}"

def area_rombo(diagonal_mayor, diagonal_menor):
    try:
        validar(diagonal_mayor, diagonal_menor)
        """Calcula el área de un rombo dado las diagonales.
           Retorna el área calculada del rombo.
             Parámetros:
                  diagonal_mayor (float): La longitud de la diagonal mayor del rombo.
                  diagonal_menor (float): La longitud de la diagonal menor del rombo.
                  area = (diagonal_mayor * diagonal_menor) / 2
                    return area
        """
        area = (diagonal_mayor * diagonal_menor) / 2
        return area
    except Exception as e:
        return f"Error en área_rombo: {e}"

def area_romboide(base, altura):
    try:
        validar(base, altura)
        """Calcula el área de un romboide dado la base y la altura.
           Retorna el área calculada del romboide.
             Parámetros:
                  base (float): La longitud de la base del romboide.
                  altura (float): La altura del romboide.
                  area = base * altura
                    return area
        """
        area = base * altura
        return area
    except Exception as e:
        return f"Error en área_romboide: {e}"

def area_trapecio(base_mayor, base_menor, altura):
    try:
        validar(base_mayor, base_menor, altura)
        """Calcula el área de un trapecio dado las bases y la altura.
           Retorna el área calculada del trapecio.
             Parámetros:
                  base_mayor (float): La longitud de la base mayor del trapecio.
                  base_menor (float): La longitud de la base menor del trapecio.
                  altura (float): La altura del trapecio.
                  area = ((base_mayor + base_menor) * altura) / 2
                    return area
        """
        area = (base_mayor + base_menor) * altura / 2
        return area
    except Exception as e:
        return f"Error en área_trapecio: {e}"

def area_pentagono(lado, apotema):
    try:
        validar(lado, apotema)
        """Calcula el área de un pentágono dado el lado y el apotema.
           Retorna el área calculada del pentágono.
             Parámetros:
                  lado (float): La longitud del lado del pentágono.
                  apotema (float): La longitud del apotema del pentágono.
                  area = (lado * apotema) / 2
                    return area
        """
        area = (lado * apotema) / 2
        return area
    except Exception as e:
        return f"Error en área_pentagono: {e}"
