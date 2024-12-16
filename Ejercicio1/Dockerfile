# Dockerfile para Ejercicio1
FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY src/ ./src/
COPY tests/ ./tests/
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar pruebas
CMD ["sh", "-c", "export PYTHONPATH=src && pytest --cov=src --cov-report=term"]

