from Crypto.PublicKey import RSA

#Lectura del .pem BEGIN RSA PRIVATE KEY
with open("C:\\Users\\Dami\\Documents\\UCE\\S8-S9\\Criptografía y seguridad de la información\\python_cripto\\general\\FORMATOS DE DATOS\\privacy_enhanced_mail.pem") as f:
    private_key_pem = f.read()

clave_privada = RSA.import_key(private_key_pem) #Obtencion de la clave privada

print("clave_privada")
print(clave_privada)
#decimal = int(clave_privada) error
print("RSA modulus")
print(clave_privada.n) #RSA modulus
print("RSA public exponent")
print(clave_privada.e) #RSA public exponent
print("RSA private exponent")
print(clave_privada.d) #RSA private exponent
