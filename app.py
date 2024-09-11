import json
import csv
import requests
import argparse

# Función para obtener datos del clima


def obtener_datos_clima(ciudad, formato):
    api_key = 'd81d727f1ed6666de01304257cd19b66'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={
        ciudad}&appid={api_key}&units=metric&lang=es'

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción para errores de HTTP
        datos = respuesta.json()

        # Verificar si el servidor devuelve un error en el campo 'cod'
        if datos.get('cod') != 200:
            return f"Error: {datos.get('message', 'No se encontraron datos para la ciudad especificada.')}"

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

    except requests.exceptions.HTTPError as http_err:
        return f"Error HTTP: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Error de conexión: No se pudo conectar con el servidor."
    except requests.exceptions.Timeout:
        return "Error de tiempo de espera: La solicitud al servidor tardó demasiado."
    except requests.exceptions.RequestException as err:
        return f"Error en la solicitud: {err}"

# Configuración de argparse


def configurar_parser():
    help_message = """
    Uso: app.py --ciudad [CIUDAD] --formato [FORMATO]

    Esta CLI te permite obtener los datos del clima para cualquier ciudad del mundo.

    Opciones:
      --ciudad     Especifica la ciudad para la cual quieres obtener los datos del clima. Ejemplo: --ciudad Madrid
      
      --formato    Especifica el formato en el cual deseas recibir los datos. Las opciones disponibles son:
                     - JSON  : Para recibir los datos en formato JSON.
                     - CSV   : Para recibir los datos en formato CSV.
                     - Texto : Para recibir los datos en un formato de texto simple.
      
      --help       Muestra este mensaje de ayuda y termina la ejecución.

    Ejemplos de uso:
      python app.py --ciudad Madrid --formato JSON
      python app.py --ciudad "New York" --formato Texto
      python app.py --ciudad Tokyo --formato CSV
    """

    parser = argparse.ArgumentParser(
        description="Esta CLI te permite obtener los datos del clima para cualquier ciudad del mundo.",
        epilog=help_message,
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
