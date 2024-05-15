import hashlib
import binascii
import time

#Rura del archivo

#filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\10palabras.txt'
#filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\100palabras.txt'
#filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\1000palabras.txt'
#filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\10000palabras.txt'
#filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\100000palabras.txt'
filename = 'C:\\Users\\fabri\\OneDrive\\Documentos\\Proyectos\\Proyecto1\\palabras\\1000000palabras.txt'



# Iniciar el temporizador para la lectura
start_time_read = time.time()

# Leer el archivo
with open(filename, 'rb') as f:
    data = f.read()  # Lee el txt

# Calcular el tiempo de lectura
elapsed_time_read = (time.time() - start_time_read) * 1000  # Conversión a milisegundos

# Decodificar los datos
decoded_data = data.decode()

# Imprimir mensaje original
print("Mensaje original:", decoded_data)

# Obtener el número de caracteres
input_chars = len(decoded_data.replace(' ', ''))
print("Número de caracteres de entrada sin espacios:", input_chars)

# Iniciar el temporizador para el hash
start_time_hash = time.time()

# Crear el objeto hash con BLAKE2b
hash_object = hashlib.blake2b(data)  # Calcula el hash BLAKE2b de los datos

# Obtener el hash en formato hexadecimal
hex_dig = hash_object.hexdigest()  # Convierte el hash a formato hexadecimal

# Imprimir el mensaje cifrado
print("Mensaje cifrado:", hex_dig)

# Obtener el número de caracteres de salida
output_chars = len(hex_dig)
print("Número de caracteres de salida:", output_chars)

# Calcular el tiempo transcurrido para el hash
elapsed_time_hash = (time.time() - start_time_hash) * 1000  # Convertir a milisegundos

# Imprimir el tiempo transcurrido
print("Tiempo de lectura: {:.6f} milisegundos".format(elapsed_time_read))
print("Tiempo de hash: {:.6f} milisegundos".format(elapsed_time_hash))
