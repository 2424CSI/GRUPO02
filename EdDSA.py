import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

def generar_par_claves():
    tiempo_inicio = time.time() * 1000
    clave_privada = ed25519.Ed25519PrivateKey.generate()
    clave_publica = clave_privada.public_key()
    tiempo_fin = time.time() * 1000
    tiempo_generacion_llave = tiempo_fin - tiempo_inicio
    return clave_privada, clave_publica, tiempo_generacion_llave

def firmar_archivo(clave_privada, archivo):
    tiempo_inicio = time.time() * 1000
    with open(archivo, "r") as f: 
        tiempo_inicio_lectura = time.time() * 1000
        mensaje_completo = f.read().encode('utf-8')
        tiempo_fin_lectura = time.time() * 1000
        tiempo_lectura = tiempo_fin_lectura - tiempo_inicio_lectura
        print("Tiempo de lectura:", tiempo_lectura, "milisegundos")
        palabras = mensaje_completo.decode('utf-8').split()[:1000]  
        print("Texto original (solo las 1ras 1000 palabras):", ' '.join(palabras))
        
    firma = clave_privada.sign(mensaje_completo)
    tiempo_fin = time.time() * 1000
    tiempo_cifrado = tiempo_fin - tiempo_inicio
    
    print("Texto cifrado:", firma.hex())
    print("Número de caracteres del texto cifrado:", len(firma))
    return firma, tiempo_cifrado

def verificar_firma(clave_publica, archivo, firma):
    tiempo_inicio = time.time() * 1000
    with open(archivo, "r") as f:  
        mensaje_completo = f.read().encode('utf-8')
        palabras = mensaje_completo.decode('utf-8').split()[:1000]  
        print("Texto cifrado:", firma.hex())
    try:
        clave_publica.verify(firma, mensaje_completo)
        tiempo_fin = time.time() * 1000
        tiempo_descifrado = tiempo_fin - tiempo_inicio
        print("Texto descifrado (solo las 1ras 1000 palabras):", ' '.join(palabras))
        return tiempo_descifrado
    except:
        return 0

def ejecutar():
    archivos = [
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\10palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\100palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\1000palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\10000palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\100000palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\1000000palabras.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSAGrupal\\10000000palabras.txt"
    ]

    for archivo in archivos:
        print(f"\nProcesando archivo: {archivo}")

        
        clave_privada, clave_publica, tiempo_generacion_llave = generar_par_claves()

        print("Clave privada:", clave_privada.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        ))
        print("Clave pública:", clave_publica.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        ))
        
        print("Firma:")
        firma, tiempo_cifrado = firmar_archivo(clave_privada, archivo)

        tiempo_descifrado = verificar_firma(clave_publica, archivo, firma)

        print("Tiempo de generación de llave:", tiempo_generacion_llave, "milisegundos")
        print("Tiempo de cifrado:", tiempo_cifrado, "milisegundos")
        print("Tiempo de descifrado:", tiempo_descifrado, "milisegundos")
        print("")

print("Resultados")
ejecutar()
