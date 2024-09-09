#!/bin/bash

# Activar entorno virtual en Windows usando Git Bash
source .venv/Scripts/activate

# Aquí metemos las pruebas más básicas
echo "Probando con formato JSON..."
python app.py --ciudad Madrid --formato JSON

echo "Probando con formato CSV..."
python app.py --ciudad Tokyo --formato CSV

echo "Probando con formato Texto..."
python app.py --ciudad "Asuncion" --formato Texto

echo "Pruebas completadas."
