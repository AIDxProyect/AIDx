import platform
import psutil
import socket
import subprocess
import winreg
import os
import wmi
import nmap
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp



def obtener_informacion_sistema():
    informacion = {}

    # Información del sistema operativo
    informacion['Sistema Operativo'] = platform.system()
    informacion['Versión'] = platform.version()
    informacion['Arquitectura'] = platform.machine()

    # Información del hardware
    informacion['Procesador'] = platform.processor()
    informacion['Memoria Total'] = psutil.virtual_memory().total
    informacion['Memoria Disponible'] = psutil.virtual_memory().available

    # Información de red
    informacion['Dirección IP'] = obtener_direccion_ip()
    informacion['Dirección MAC'] = obtener_direccion_mac()

    # Verificación de actualizaciones del sistema operativo
    actualizaciones = obtener_actualizaciones()
    informacion['Actualizaciones disponibles (nombres)'] = actualizaciones

   
    return informacion


def obtener_direccion_ip():
    # Obtener la dirección IP del equipo
    direccion_ip = socket.gethostbyname(socket.gethostname())
    return direccion_ip


def obtener_direccion_mac():
    interfaces = psutil.net_if_addrs()
    for interfaz in interfaces:
        if interfaz != 'lo':
            for direccion in interfaces[interfaz]:
                if direccion.family == psutil.AF_LINK:
                    return direccion.address

    return "Dirección MAC no encontrada"


def obtener_actualizaciones():
    actualizaciones = []
    c = wmi.WMI()
    for update in c.Win32_QuickFixEngineering():
        if update.HotFixID is not None:
            actualizaciones.append(update.Caption)

    return actualizaciones




def generar_archivo_infectado(informacion_sistema):
    ruta_archivo_infectado = os.path.join(os.path.expanduser("~"), "Desktop", "files", "info_equipo_infectado.txt")

    with open(ruta_archivo_infectado, 'w') as archivo_infectado:
        for clave, valor in informacion_sistema.items():
            archivo_infectado.write(f"{clave}: {valor}\n")

    print("Archivo 'info_equipo_infectado.txt' creado con éxito en la carpeta 'files'.")


if __name__ == '__main__':
    
    informacion_sistema = obtener_informacion_sistema()

    ruta_carpeta_files = os.path.join(os.path.expanduser("~"), "Desktop", "files")
    if not os.path.exists(ruta_carpeta_files):
        os.makedirs(ruta_carpeta_files)

    generar_archivo_infectado(informacion_sistema)