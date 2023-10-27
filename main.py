import os
import unidecode
import logging

def configurar_registro():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler('renombrar_archivos.log'),
                                  logging.StreamHandler()])

def sanitizar_nombre_archivo(nombre_archivo):
    sanitizado = nombre_archivo.replace(' ', '_')  # Reemplaza espacios con guiones bajos
    sanitizado = unidecode.unidecode(sanitizado)  # Elimina acentos de los caracteres
    sanitizado = sanitizado.replace('ñ', 'n').replace('Ñ', 'N')  # Reemplaza ñ y Ñ con n y N respectivamente
    return sanitizado

def renombrar_archivos_en_directorio(ruta_directorio):
    for nombre_archivo in os.listdir(ruta_directorio):
        ruta_antigua = os.path.join(ruta_directorio, nombre_archivo)
        nuevo_nombre_archivo = sanitizar_nombre_archivo(nombre_archivo)
        nueva_ruta = os.path.join(ruta_directorio, nuevo_nombre_archivo)
        try:
            os.rename(ruta_antigua, nueva_ruta)
            logging.info(f'Renombrado exitoso de {ruta_antigua} a {nueva_ruta}')
        except Exception as e:
            logging.error(f'Error renombrando {ruta_antigua} a {nueva_ruta}: {e}')

if __name__ == '__main__':
    configurar_registro()
    ruta_directorio = input("Ingrese la ruta del directorio: ")
    if os.path.isdir(ruta_directorio):
        renombrar_archivos_en_directorio(ruta_directorio)
    else:
        logging.error(f'La ruta especificada {ruta_directorio} no es un directorio')
        print(f'Error: La ruta especificada {ruta_directorio} no es un directorio')
