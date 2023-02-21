# Función para convertir de decimal a hexadecimal
def decimal_hexadecimal(num_dec):
    return hex(num_dec)[2:].upper()

# Función para procesar una línea de texto
def proceso(linea):
    cadenas = linea.strip().split(',')
    segunda_cadena = cadenas[2].strip()
    # Obtener la dirección IP y convertirla a hexadecimal
    direccion_ip = cadenas[-1].strip()
    partes_ip = direccion_ip.split('.')
    direccion_hexadecimal = '.'.join([decimal_hexadecimal(int(partes)) for partes in partes_ip])
    # Obtener los números en decimal
    numeros_decimales = [str(int(x, 16)) for x in cadenas[0].split('/')[0].split(':')]
    resultado = f"{segunda_cadena} : {' : '.join(numeros_decimales)} : {direccion_hexadecimal}\n"
    return resultado

entrada = "E:/SSPSO/prueba2.txt"
salida = "E:/SSPSO/resultado.txt"

with open(entrada, 'r') as en, open(salida, 'w') as sa:
    for linea in en:
        sa.write(proceso(linea))
en.close()
sa.close()


