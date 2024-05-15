import time
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generar_pares_claves():
    clave_privada = ec.generate_private_key(ec.SECP256R1(), default_backend())
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica

def sign_message(private_key, mensaje):
    firma = private_key.sign(
        mensaje,
        ec.ECDSA(hashes.SHA256())
    )
    return firma

def verificar_firma(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print("Error:", e)
        return False

def main():
      # Iniciar temporizador para la lectura del archivo
    inicio_tiempo_lectura = time.time()

    # Leer el archivo con el texto del mensaje a cifrar
    with open("10000000palabras.txt",'rb') as f:
        msj_original = f.read()
    print("Número de caracteres de entrada:", len(msj_original.replace(b" ",b"")))
# Finalizar temporizador para la lectura del archivo
    fin_tiempo_lectura = time.time()
    print("Tiempo para leer el archivo:", (fin_tiempo_lectura - inicio_tiempo_lectura)*1000, "milisegundos")

    # Generar e imprimir la clave de cifrado (y de descifrado)
    tiempo_inicio = time.time()
    clave_privada, clave_publica = generar_pares_claves()
    tiempo_final = time.time()
    print("Tiempo para generar las claves:", (tiempo_final - tiempo_inicio)*1000, "milisegundos")

    # Antes de cifrar
    #print("Texto antes de cifrar:", original_message.decode("utf-8"))

    # Cifrar e imprimir el texto
    tiempo_inicio = time.time()
    firma = sign_message(clave_privada, msj_original)
    tiempo_final = time.time()
    print("Tiempo para cifrar el texto:", (tiempo_final - tiempo_inicio)*1000, "milisegundos")
    print("Número de caracteres durante el cifrado:", len(firma))
    print("Firma digital:", firma.hex())

    # Descifrar e imprimir el texto
    tiempo_inicio = time.time()
    verifica_si = verificar_firma(clave_publica, msj_original, firma)
    tiempo_final = time.time()
    print("Tiempo para descifrar el texto:", (tiempo_final - tiempo_inicio)*1000, "milisegundos")
    if verifica_si:
        print("La firma digital es válida.")
        print("Texto cifrado:", firma.hex())
    else:
        print("La firma digital no es válida.")

    decifrar_mensaje = ""
    if verifica_si:
        decifrar_mensaje = msj_original
    #print("Texto descifrado:", decrypted_message.decode("utf-8"))
    print("Número de caracteres de salida:", len(decifrar_mensaje))

if __name__ == "__main__":
    main()