import math

#Santiago Coronado Pinzon.
#Libreria de complejos


def sumacomplejos(a,b):
    # Suma de numeros complejos
    real = a[0]+b[0]
    img = a[1]+b[1]
    return real,img

def multiplicacioncomplejos(a,b):
    # Multiplicacion de numeros complejos
    real = (a[0]*b[0])-(a[1]*b[1])
    img = (a[0]*b[1])+(b[0]*a[1])
    return real,img

def restacomplejos(a,b):
    # Resta de numeros complejos
    real = a[0]-b[0]
    img = a[1]-b[1]
    return real,img

def divicioncomplejos(a,b):
    # Division de numeros complejos
    try:
        div = b[0] ** 2 + b[1] ** 2
        real = (a[0] * b[0] + a[1] * b[1]) / div
        img = (a[1] * b[0] - a[0] * b[1]) / div
        return (real, img)
    except:
        return 'Imposible hacer la division.'


def modulocomplejos(c):
    # Modulacion de numeros complejos
    modulo = (c[0] ** 2 + c[1] ** 2)
    return round(math.sqrt(modulo),2)


def conjugadocomplejos(c):
    # Conjugado de numeros Complejos
    real = c[0]
    img = c[1] * -1
    return real, img

def polar_cartiaciono(c):
    # Conversion de polar a cartesiano
    real = round(c[0] * math.cos(c[1]),2)
    img = round(c[0] * math.sin(c[1]),2)
    return real,img

def fasecomplejos(c):
    # Retornar la fase de un numero complejo
    if c[0] < 0 and c[1] < 0:
        phase = round(2 * math.pi - (-1 * (math.atan2(c[1], c[0]))), 2)
        return phase
    elif c[0] > 0 > c[1]:
        phase = round((2 * math.pi + math.atan2(c[1], c[0])),2)
        return phase
    else:
        phase = round((math.atan2(c[1], c[0])),2)
        return phase

def to_String(c):
    print(str(c[0]) + "+" + str(c[1]) + "i")

if __name__ == "__main__":
    c = (4,4)
    to_String(sumacomplejos((4,-3),(12,9)))
    to_String(multiplicacioncomplejos((2,3),(4,7)))
    to_String(restacomplejos((2,3),(4,7)))
    to_String(divicioncomplejos((2,3),(4,7)))
    print((modulocomplejos(c)))
    to_String(polar_cartiaciono((64,33)))
    print(((c)))
    print(fasecomplejos(c))
