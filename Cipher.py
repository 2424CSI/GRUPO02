import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import time

# Obtener la ruta del directorio en el que se encuentra el script
directorio_actual = os.path.dirname(__file__)

# Ruta de la carpeta de textos
directorio_textos = os.path.join(directorio_actual, 'palabras')

# Archivos txt:
ruta_archivo = os.path.join(directorio_textos, "10palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "100palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "1000palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "10000palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "100000palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "1000000palabras.txt")
#ruta_archivo = os.path.join(directorio_textos, "10000000palabras.txt")

print("Directorio actual de trabajo:", directorio_actual)
print("Ruta del archivo:", ruta_archivo)

def generar_clave():
    return os.urandom(32)  # Clave de 256 bits para AES

def cifrar(clave, mensaje):
    iv = os.urandom(16)  # Vector de inicialización único
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    mensaje_cifrado = encryptor.update(mensaje) + encryptor.finalize()
    return iv, mensaje_cifrado

def descifrar(clave, iv, mensaje_cifrado):
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    mensaje_descifrado = decryptor.update(mensaje_cifrado) + decryptor.finalize()
    return mensaje_descifrado

def contar_caracteres_sin_espacios(texto):
    # Eliminar espacios y contar caracteres
    return len(texto.replace(b" ", b""))

# Etapa 1: Leer el archivo con el texto del mensaje a cifrar
inicio = time.perf_counter()
with open(ruta_archivo, "rb") as archivo_mensaje:
    texto_original = archivo_mensaje.read()
tiempo_etapa1 = (time.perf_counter() - inicio) * 1000  #Tiempo

# Contar caracteres sin espacios en el texto original
caracteres_originales_sin_espacios = contar_caracteres_sin_espacios(texto_original)

# Etapa 2: Generar e imprimir la clave de cifrado y descifrado
inicio = time.perf_counter()
clave = generar_clave()
#print("Clave de cifrado y descifrado:", clave)
tiempo_etapa2 = (time.perf_counter() - inicio) * 1000  #Tiempo

# Etapa 3: Cifrar e imprimir el texto
inicio = time.perf_counter()
iv, mensaje_cifrado = cifrar(clave, texto_original)
#print("Texto cifrado:", mensaje_cifrado)
tiempo_etapa3 = (time.perf_counter() - inicio) * 1000  #Tiempo

# Etapa 4: Descifrar e imprimir el texto
inicio = time.perf_counter()
mensaje_descifrado = descifrar(clave, iv, mensaje_cifrado)
#print("Texto descifrado:", mensaje_descifrado)
tiempo_etapa4 = (time.perf_counter() - inicio) * 1000  #Tiempo

# Contar caracteres sin espacios en el texto cifrado
caracteres_cifrados_sin_espacios = contar_caracteres_sin_espacios(mensaje_cifrado)

# Imprimir el número de caracteres sin espacios
#print("Número de caracteres originales sin espacios:", caracteres_originales_sin_espacios)
print("Número de caracteres descifrados sin espacios:", caracteres_cifrados_sin_espacios)

# Imprimir el tiempo transcurrido en cada etapa
print("Tiempo transcurrido en la Etapa 1 (Leer el archivo):", tiempo_etapa1, "milisegundos")
print("Tiempo transcurrido en la Etapa 2 (Generar e imprimir la clave):", tiempo_etapa2, "milisegundos")
print("Tiempo transcurrido en la Etapa 3 (Cifrar):", tiempo_etapa3, "milisegundos")
print("Tiempo transcurrido en la Etapa 4 (Descifrar):", tiempo_etapa4, "milisegundos")


