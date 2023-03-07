# Módulo que contiene las funciones encargadas de hacer conversiones de bases numéricas

# Decimal a binario
def dec_a_bin(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario


# Hexadecimal a binario

def hex_a_bin(ini_string):

    scale = 16
  
    # Printing initial string
    print ("Initial string", ini_string)
    
    # Code to convert hex to binary
    res = bin(int(ini_string, scale)).zfill(8)
    
    # Print the resultant string
    print ("Resultant string", str(res))

hex_a_bin("1ABC")
