# Importamos las librerías necesarias
from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
import base64
import codecs

# Establecemos una conexión remota con el servidor de cryptohack
r = remote('socket.cryptohack.org', 13377, level = 'debug')

# Función para recibir datos en formato JSON
def json_recv():
    line = r.recvline()   # Recibimos los datos
    return json.loads(line.decode()) #retorna los datos decodificados tipo JSON

# Función para enviar datos en formato JSON
def json_send(hsh):
    request = json.dumps(hsh).encode() #Conbierte el diccionario hsh en cadena de texto JSON, 
    # y Codifica la cadena JSON en una secuencia de bytes
    r.sendline(request) #envia la solicitud JSON

# Iteramos 100 veces
for i in range(100):
    received = json_recv() #guardo el JSON en received

    #Imprimo el tipo y el encoded value
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    tipo=received["type"]
    encoded1=received["encoded"]

    # Decodificación según el tipo recibido
    if (tipo =="bigint"): 
        long_value = int(encoded1, 16) #pasa de hexadecimal a entero
        print("long_value: ")
        print(long_value)
        bytes_value=long_to_bytes(long_value) #de entero a bytes
        decoded=bytes_value.decode("utf-8") #de bytes a string

    elif (tipo =="rot13"):
        value=codecs.encode(encoded1, 'rot_13') # rota 13 pociciones del alfabeto 
        print("value: ")
        print(value)
        decoded=value #string
    elif (tipo =="base64"):
        bytes_value = base64.b64decode(encoded1) #decodifica de base 64 a bytes
        decoded = bytes_value.decode('utf-8') #de bytes a string
    elif (tipo =="hex"):
        bytes_value = bytes.fromhex(encoded1) #de hexadecimal a bytes
        decoded = bytes_value.decode('utf-8') #de bytes a string
    elif (tipo =="utf-8"):
        decoded = ''.join(chr(num) for num in encoded1) #de array de numeros a char y a String

    print("decoded: ")
    print(decoded)

    #creo el  Json con el resultado
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

received = json_recv()


