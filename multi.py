# Multiplicador combinacional
#
# Valores de entrada:  - Tipo decimal, hecadecimal y binario
#                      - Para indicar la base numérica de los factores, se utilizará una letra delante del número de la siguiente
#                        forma: d25, h2a y b10. 
#                      - En caso de no indicarlo el usuario, se tomará el número como decimal
#                      - El programa debe ser ejecutado desde comando de consola. Ejemplo: mult.py --bits 6 -a d21 -b h10
#
# Valores de salida:   - Mostrar resultado en binario
# 

import algoritmo
import conversion

def multiplicarFacil (num1, num2):
    
    num1 = str(num1)
    num2 = str(num2)
 
    Multiplication = int(num1, 2) * int(num2, 2)
    binaryMul = bin(Multiplication)
 
    print("\nResultado FACIL = " + binaryMul)


# bits = int
# num1, num2 = string
# main function

def multi (bits, num1, num2):

    bin1 = 0
    bin2 = 0

    lista1 = list(num1)
    lista2 = list(num2)


    if (verificarEntrada(num1, bits) == 1 and lista1[0] == "d"):
        bin1 = conversion.dec_a_bin(int(num1[1:]))
    
    elif (verificarEntrada(num1, bits) == 1):
        bin1 = conversion.dec_a_bin(int(num1))

    elif (verificarEntrada(num1, bits) == 2):
        bin1 = int(num1[1:])
    
    elif (verificarEntrada(num1, bits) == 3):
        temp = conversion.hex_a_bin(num1[1:])
        bin1 = int(temp[2:])

    else:
        print ("El siguiente valor de entrada no es permitido: " + num1)
        return False
    

    if (verificarEntrada(num2, bits) == 1 and lista1[0] == "d"):
        bin2 = conversion.dec_a_bin(int(num2[1:]))
    
    elif (verificarEntrada(num2, bits) == 1):
        bin2 = conversion.dec_a_bin(int(num2))

    elif (verificarEntrada(num2, bits) == 2):
        bin2 = int(num2[1:])
    
    elif (verificarEntrada(num2, bits) == 3):
        temp = conversion.hex_a_bin(num2[1:])
        bin2 = int(temp[2:])

    else:
        print ("El sieguiente valor de entrada no es permitido: " + num2)
        return False
    
    
    print(algoritmo.operar(bin1, bin2))
    return True


    


# Verifica la base numérica de la entrada
# Posibles salidas:
# 0 : entrada invalida
# 1 : decimal
# 2 : binario
# 3 : hexadecimal
def verificarEntrada (num, bits):

    list_num = list(num)
    temp_list = list(num)
    del temp_list[0]

    if (len(list_num) > bits):
        print("El valor excede el límite de bits")
        return 0

    elif (len(list_num) == 0):
        print("El valor es inválido")
        return 0

    elif (verificarDecimal(list_num) == True):
        print("El valor es decimal")
        return 1


    elif (list_num[0] == "b" and verificarBinario(temp_list) == True):
        print("El valor es binario")
        return 2

    elif (list_num[0] == "d" and verificarDecimal(temp_list) == True):
        print("El valor es decimal")
        return 1
    
    elif (list_num[0] == "h" and verificarHexadecimal(temp_list) == True):
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
        if (n == "0" or n == "1"):
            True
        else:
            print("No es binario")
            return False

    print ("Es BINARIO")
    return True


# Verifica si en una lista de numeros solo hay valores hexadecimales 
def verificarHexadecimal (list_num):
    lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F"]
    for n in list_num:
        if n in lst :
            True
        else:
            print("No es hexadecimal")
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

##multiplicarFacil (1111, 110)

#print(algoritmo.operar(1011, 1110))

multi (10, "h1A1", "123")

#verificarHexadecimal(["1", "H", "0"])

##verificarEntrada("b151", 5)

