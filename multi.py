# Multiplicador combinacional
#
# Valores de entrada:  - Tipo decimal, hecadecimal y binario
#                      - Para indicar la base numérica de los factores, se utilizará una letra delante del número de la siguiente
#                        forma: d25, h2a y b10. 
#                      - En caso de no indicarlo el usuario, se tomará el número como decimal
#                      - El programa debe ser ejecutado desde comando de consola. Ejemplo: mult.py --bits 6 -a d21 -b h10
#
# Valores de salida:   - Mostrar resultado en binaario
# 

import algoritmo
import conversion

def multiplicarFacil (num1, num2):
    
    num1 = str(num1)
    num2 = str(num2)
 
    Multiplication = int(num1, 2) * int(num2, 2)
    binaryMul = bin(Multiplication)
 
    print("\nResultado FACIL = " + binaryMul)



def multi (bits, num1, num2):

    lista = list(num1)
    print(lista)



# Verifica la base numérica de la entrada
# Posibles salidas:
# 0 : entrada invalida
# 1 : decimal
# 2 : binario
# 3 : hexadecimal
def verificarEntrada (num, bits):

    list_num, temp_list = list(num)
    del temp_list[0]

    if (len(list_num) > bits):
        print("El valor excede el límite de bits")
        return 0

    if (len(list_num) == 0):
        print("El valor es inválido")
        return 0

    elif (verificarDecimal(list_num) == True):
        print("El valor es decimal")
        return conversion.dec_a_bin(num)


    elif (list_num[0] == "b"):
        print("El valor es binario")
        return 2

    elif (list_num[0] == "d" and verificarDecimal(temp_list) == True):
        print("El valor es decimal")
        return 1
    
    elif (list_num[0] == "h"):
        print("El valor es hexadecimal")
        return 3
    
    else:
        print("Valor inválido")
        return 0

 

#Verifica si una lista contiene solo números
# La entrada debe ser una lista
def verificarDecimal (list_num):

    for n in list_num:
        if (isNumeric(n) == False):
            return False

    return True

# Verifica si en una lista de numeros solo hay valores binarios 
def verificarBinario (list_num):
    for n in list_num:
        print (n)
        if (n != '0' or n != '1'):
            print("no es binario")
            return False

    return True


# Verifica si en una lista de numeros solo hay valores hexadecimales 
def verificarHexadecimal (list_num):

    for n in list_num:
        if (n != "A" or n != "B" or n != "C" or n != "D" or n != "E" or n != "F" ):
            return False

    return True

# Verifica si un valor es numérico o puede convertirse en integer
def isNumeric(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

### Pruebas

#multiplicarFacil (1011, 1110)

print(algoritmo.operar(1011, 1110))

#multi (1, "d123", 123)

#verificarTodosNumeros(["d","1"])

#verificarEntrada("b151")