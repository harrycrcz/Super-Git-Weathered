#!/bin/bash

source .venv/Scripts/activate

#Aca metemos las pruebas mas basicas
echo "Probando con formato JSON..."
python3 clima_cli.py --ciudad Madrid --formato JSON

echo "Probando con formato CSV..."
python3 clima_cli.py --ciudad Tokyo --formato CSV

echo "Probando con formato Texto..."
python3 clima_cli.py --ciudad "Asuncion" --formato Texto

echo "Pruebas completadas."
