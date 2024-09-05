import json
import csv
import requests
import argparse

# Función para obtener datos del clima


def obtener_datos_clima(ciudad, formato):
    api_key = 'd81d727f1ed6666de01304257cd19b66'
    url = f'''http://api.openweathermap.org/data/2.5/weather?q={
        ciudad}&appid={api_key}&units=metric&lang=es'''
    respuesta = requests.get(url)
    datos = respuesta.json()

    if formato == 'JSON':
        return json.dumps(datos, indent=4)
    elif formato == 'CSV':
        nombre_archivo = f'{ciudad}_clima.csv'
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for clave, valor in datos.items():
                escritor_csv.writerow([clave, valor])
        return f"Datos guardados en {nombre_archivo}"
    elif formato == 'Texto':
        descripcion = datos['weather'][0]['description']
        temp = datos['main']['temp']
        humedad = datos['main']['humidity']
        return f'Clima en {ciudad}:\nDescripción: {descripcion}\nTemperatura: {temp}°C\nHumedad: {humedad}%'
    else:
        return 'Formato no reconocido'

# Configuración de argparse


def configurar_parser():
    help_message = """
    Uso: clima_cli.py --ciudad [CIUDAD] --formato [FORMATO]

    Esta CLI te permite obtener los datos del clima para cualquier ciudad del mundo.

    Opciones:
      --ciudad     Especifica la ciudad para la cual quieres obtener los datos del clima. Ejemplo: --ciudad Madrid
      
      --formato    Especifica el formato en el cual deseas recibir los datos. Las opciones disponibles son:
                     - JSON  : Para recibir los datos en formato JSON.
                     - CSV   : Para recibir los datos en formato CSV.
                     - Texto : Para recibir los datos en un formato de texto simple.
      
      --help       Muestra este mensaje de ayuda y termina la ejecución.

    Ejemplos de uso:
      python clima_cli.py --ciudad Madrid --formato JSON
      python clima_cli.py --ciudad "New York" --formato Texto
      python clima_cli.py --ciudad Tokyo --formato CSV
    """

    parser = argparse.ArgumentParser(
        description="Esta CLI te permite obtener los datos del clima para cualquier ciudad del mundo.",
        epilog=help_message,
        # Para que el formato del mensaje de ayuda se respete
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--ciudad', type=str, required=True,
                        help="Especifica la ciudad para la cual quieres obtener los datos del clima. Ejemplo: --ciudad Madrid")
    parser.add_argument('--formato', type=str, choices=['JSON', 'CSV', 'Texto'], required=True,
                        help="Especifica el formato en el cual deseas recibir los datos. Opciones: JSON, CSV, Texto.")
    return parser


def main():
    parser = configurar_parser()
    args = parser.parse_args()

    datos_clima = obtener_datos_clima(args.ciudad, args.formato)
    print(datos_clima)


if __name__ == "__main__":
    main()
