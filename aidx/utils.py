from cryptography.fernet import Fernet, InvalidToken 
import os

def generar_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        print("El archivo de clave 'key.key' ya existe. No se generó una nueva clave.")
        
def cargar_key():
    if os.path.exists('key.key'):
        return open('key.key', 'rb').read()
    else:
        raise ValueError("No se encontró el archivo de clave 'key.key'")

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)


def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:  # Manejo adecuado de la excepción
            #print(f"Error al desencriptar el archivo: {item}. Token inválido.")
            continue  # saltar este archivo y continuar con el siguiente

        with open(item + '.temp', 'wb') as file:  # escribir en un archivo temporal
            file.write(decrypted_data)
        os.replace(item + '.temp', item)  # reemplazar el archivo original

