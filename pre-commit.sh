#!/bin/bash
# Pre-commit hook para verificar sintaxis y formatear código.

# Verificar sintaxis en archivos Python
echo "Verificando sintaxis de archivos Python..."
for file in $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$'); do
    if [[ -f $file ]]; then
        python -m py_compile "$file"
        if [ $? -ne 0 ]; then
            echo "Error de sintaxis en $file"
            exit 1
        fi
    fi
done

# Formatear archivos Python con black
echo "Formateando archivos Python con black..."
for file in $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$'); do
    if [[ -f $file ]]; then
        black "$file"
        git add "$file"
    fi
done

# Verificar sintaxis en scripts Bash
echo "Verificando sintaxis de scripts Bash..."
for file in $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.sh$'); do
    if [[ -f $file ]]; then
        bash -n "$file"
        if [ $? -ne 0 ]; then
            echo "Error de sintaxis en $file"
            exit 1
        fi
    fi
done

echo "Todo está bien, procediendo con el commit."
exit 0